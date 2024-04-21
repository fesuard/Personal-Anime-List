from django.db import models
from userManagement.models import CustomUser


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


class UserAnime(models.Model):
    SCORE = [
        (1, '(1) Appalling'),
        (2, '(2) Horrible'),
        (3, '(3) Very Bad'),
        (4, '(4) Bad'),
        (5, '(5) Average'),
        (6, '(6) Fine'),
        (7, '(7) Good'),
        (8, '(8) Very Good'),
        (9, '(9) Great'),
        (10, '(10) Masterpiece')
    ]
    WATCH_STATUS = [
        ('watching', 'Watching'),
        ('completed', 'Completed'),
        ('on-hold', 'On-hold'),
        ('dropped', 'Dropped'),
        ('plan_to_watch', 'Plan to Watch'),
    ]
    watch_status = models.CharField(max_length=50, choices=WATCH_STATUS)
    eps_seen = models.IntegerField(default=0)
    score = models.IntegerField(choices=SCORE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return self.score
