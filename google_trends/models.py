from django.db import models


class Trend(models.Model):
    title = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

