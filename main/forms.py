from django.forms import ModelForm
from .models import Video

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


class MovieForm(VideoForm):
    pass

class SerialForm(VideoForm):
    pass