from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Anime(models.Model):
    STATUS = [
        ('ONGOING', 'ongoing'),
        ('FINISHED', 'finished'),
        ('UPCOMING', 'upcoming'),
        ('UNKNOWN', 'unknown'),
    ]
    TYPE = [
        ('SPECIAL', 'special'),
        ('TV', 'tv'),
        ('MOVIE', 'movie'),
        ('OVA', 'ova'),
        ('ONA', 'ona'),
        ('UNKNOWN', 'unknown'),
    ]
    SEASON = [
        ('SPRING', 'spring'),
        ('SUMMER', 'summer'),
        ('WINTER', 'winter'),
        ('FALL', 'fall'),
    ]
    title = models.CharField(max_length=300)
    type = models.CharField(max_length=100, choices=TYPE)
    episodes = models.CharField(max_length=10)
    status = models.CharField(max_length=80, choices=STATUS)
    year = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=80, choices=SEASON)
    picture = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    relatedAnime = models.CharField(max_length=8000)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
