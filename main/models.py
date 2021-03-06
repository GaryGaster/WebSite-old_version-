from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField


class Video(models.Model):
    PLATFORMS = {
        (1, 'HBO'),
        (2, 'NETFLIX'),
        (3, 'AMAZONPRIME'),
        (4, 'YOUTUBE'),
        (5, 'CDA'),
    }

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')
    year = models.IntegerField(null=True, blank=True)
    platforms = MultiSelectField(null=True, blank=True, choices=PLATFORMS)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    votes_total = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, related_name='video_voters')
    image = models.ImageField(null=True, blank=True, default='video-default.jpg', upload_to='media/')
    url = models.URLField(blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def title_year(self):
        return self.title + " (" + str(self.year) + ") "

    def timestamp_pretty(self):
        return self.timestamp.strftime('%-H:%M; %d.%m.%Yr.')

    def updated_pretty(self):
        return self.updated.strftime('%-H:%M %d.%m.%Yr.')

    class Meta:
        abstract = True


class Movie(Video):
    voters = models.ManyToManyField(User, related_name='movie_voters')

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})


class Serial(Video):
    voters = models.ManyToManyField(User, related_name='serial_voters')

    def get_absolute_url(self):
        return reverse('serial-detail', kwargs={'pk': self.pk})


class Anime(Video):
    voters = models.ManyToManyField(User, related_name='anime_voters')

    def get_absolute_url(self):
        return reverse('anime-detail', kwargs={'pk': self.pk})
