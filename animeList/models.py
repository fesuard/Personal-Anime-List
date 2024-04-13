from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Anime(models.Model):
    STATUS = [
        ('ONGOING', 'Ongoing'),
        ('FINISHED', 'finished'),
        ('UPCOMING', 'upcoming'),
        ('UNKNOWN', 'unknown'),

    ]
    title = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    episodes = models.CharField(max_length=10)
    status = models.CharField(max_length=80, choices=STATUS)
    year = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=80)
    picture = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    relatedAnime = models.CharField(max_length=8000)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
