from django.db import models
from google_trends.models import Trend

class Post(models.Model):
    trend = models.ForeignKey(Trend, on_delete=models.CASCADE, null=True)

    uuid = models.CharField(max_length=2083)
    title = models.CharField(max_length=2083, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=2083, null=True, blank=True)
    snippet = models.CharField(max_length=2083, null=True, blank=True)
    url = models.CharField(max_length=2083, null=True, blank=True)
    image_url = models.CharField(max_length=2083, null=True, blank=True)
    language = models.CharField(max_length=2083, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=2083, null=True, blank=True)
    types = models.CharField(max_length=2083, null=True, blank=True)
# categories = ["general"]
# relevance_score = None
    created_on = models.DateTimeField(auto_now_add=True)
