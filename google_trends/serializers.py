from statistics import mode
from rest_framework import serializers
from google_trends.models import Trend
from news.models import Post
from news.serializers import PostSerializer

class TrendSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Trend
        fields = '__all__'

    def get_posts(self, instance):
        return [PostSerializer(post).data for post in Post.objects.filter()]
