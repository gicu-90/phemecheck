import json
import requests
from .serializers import PostSerializer
from google_trends.views import get_trends
from google_trends.models import Trend
from rest_framework import decorators, response, status


def get_news(search):
    token = 'PFcUPTaEGujCvoeluXYKVPN8EcyBVeRUsbn7C4VG'
    url = f'https://api.thenewsapi.com/v1/news/top?api_token={token}&limit=3&search={search}'

    valuation_response = requests.request('GET', url)

    decoded_response = valuation_response.content.decode('utf8')
    json_response = json.loads(decoded_response)

    return json_response


def generate():
    trends = get_trends()
    # trends = ['samsung']

    for trend in trends:
        data = get_news(trend)['data']
        
        if not data:
            continue
        
        registered_trend, is_created = Trend.objects.get_or_create(title=trend)

        for article in data:
            serializer = PostSerializer(data={**article, 'trend':registered_trend.pk})
            serializer.is_valid(raise_exception=True)
            serializer.save()
    
    
@decorators.api_view(['GET'])
def generate_news(request):
    generate()
    return response.Response({}, status.HTTP_200_OK)
