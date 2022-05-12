from pytrends.request import TrendReq

from google_trends.models import Trend
from .serializers import TrendSerializer
from rest_framework import generics, decorators


class TrendsView(generics.ListAPIView):
    queryset = Trend.objects.all().order_by('-created_on')[:10]
    serializer_class = TrendSerializer


def get_trends():

    pytrends = TrendReq(hl='en-US')

    countries = ['united_states', 'united_kingdom']

    trends = []

    def trending_searches(country):
        data = pytrends.trending_searches(country)
        for trend in data.head(10)[0].array:
            trends.append(trend)

    for country in countries:
        trending_searches(country)

    return trends
