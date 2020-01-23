from django.contrib import admin
from django.urls import path
from .views import all_movies, create_movie, update_movie, delete_movie, upvote

urlpatterns = [
    path('', all_movies, name= 'all_movies'),
    path('create_movie', create_movie, name= 'create_movie'),
    path('update_movie/<int:id>/', update_movie, name= 'update_movie'),
    path('delete_movie/<int:id>/', delete_movie, name= 'delete_movie'),
    path('<int:movie_id>/upvote/', upvote, name='upvote'),
]
