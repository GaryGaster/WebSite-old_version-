from django.forms import ModelForm
from .models import Video, Movie

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url']
        labels = {
            "title":"tytuł",
            "description":"opis",
            "year":"rok",
            "image":"zdjęcie/avatar",
            "url":"link"
        }


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url']
        labels = {
            "title":"tytuł",
            "description":"opis",
            "year":"rok",
            "image":"zdjęcie",
            "url":"link"
        }