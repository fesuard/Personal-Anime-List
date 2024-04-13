from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    episodes = models.CharField(max_length=10)
    status = models.CharField(max_length=80)
    year = models.CharField(max_length=10, null=True)
    season = models.CharField(max_length=80)
    picture = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    relatedAnime = models.CharField(max_length=8000)
    tags = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
