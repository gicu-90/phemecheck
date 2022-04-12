from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    trend_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Post
        fields = '__all__'

    def create(self, validated_data):

        validated_data['types'] = ';'.join(self.initial_data['categories'])

        post, created = models.Post.objects.get_or_create(
            uuid=validated_data.get('uuid'),
            defaults=validated_data)

        return post

    def get_trend_name(self, instance):
        if instance.trend:
            return instance.trend.title

