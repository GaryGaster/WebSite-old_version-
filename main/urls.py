from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies, name= 'all_movies'),
    path('create_movie', views.create_movie, name= 'create_movie'),
    path('update_movie/<int:id>/',  views.update_movie, name= 'update_movie'),
    path('delete_movie/<int:id>/',  views.delete_movie, name= 'delete_movie'),
    path('<int:movie_id>/upvote/',  views.upvote, name='upvote'),
]
