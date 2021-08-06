from django.db import models


class MetricsModel(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    os = models.CharField(max_length=15)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()

    def __str__(self):
        return f"{self.date},{self.channel},{self.country},{self.os}"
