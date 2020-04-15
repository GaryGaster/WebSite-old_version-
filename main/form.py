from django import forms
from .models import Video, Movie


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'year': 'Rok',
            'platforms': 'Platformy',
            'image': 'Obrazek',
            'url': 'Link',
            }


class MovieForm(VideoForm):
    pass


class SerialForm(VideoForm):
    pass


class AnimeForm(VideoForm):
    pass


class XvideoForm(VideoForm):
    pass