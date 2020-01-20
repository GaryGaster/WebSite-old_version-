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
    discription = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    platforms = MultiSelectField(null=True, blank=True, choices=PLATFORMS)
    timestamp = models.DataTimeField(auto_now=False, auto_now_add=True)
    updated = models.DataTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='images/')
    url = models.CharField(null=True, blank=True)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def summary(self):
        return self.discription[:220]


    def title_year(self):
        return self.title + " (" + str(self.year) + ") "
