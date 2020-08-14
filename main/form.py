from django import forms
from .models import Movie, Serial, Anime


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'year': 'Rok',
            'platforms': 'Platformy',
            'image': 'Obrazek',
            'url': 'Link',
        }


class SerialForm(forms.ModelForm):
    class Meta:
        model = Serial
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'year': 'Rok',
            'platforms': 'Platformy',
            'image': 'Obrazek',
            'url': 'Link',
        }


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'year': 'Rok',
            'platforms': 'Platformy',
            'image': 'Obrazek',
            'url': 'Link',
        }
