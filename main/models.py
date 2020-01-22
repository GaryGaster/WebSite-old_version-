from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Video(models.Model):
    PLATFORMS = {
        (1, 'HBO'),
        (2, 'NETFLIX'),
        (3, 'AMAZONPRIME'),
    }

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True, max_length=600)
    year = models.IntegerField(null=True, blank=True)
    platforms = MultiSelectField(null=True, blank=True, choices=PLATFORMS)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='media/')
    url = models.CharField(null=True, blank=True, max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def summary(self):
        return self.description[:220]


    def title_year(self):
        return self.title + " (" + str(self.year) + ") "

class Movie(Video):
    pass

class Serial(Video):
    pass


class Anime(Video):
    pass


class Xvideo(Video):
    pass


