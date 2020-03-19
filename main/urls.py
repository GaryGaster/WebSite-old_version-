from django.contrib import admin
from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    UserMovieListView
)
from . import views

urlpatterns = [

    path('', views.home, name= 'home'),

    #Movies
    # path('movies/', views.all_movies, name= 'all_movies'),
    path('movies/', MovieListView.as_view(), name= 'movies-home'),
    path('movies/user/<str:username>', UserMovieListView.as_view(), name= 'user-movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name= 'movie-detail'),
    path('movies/new/', MovieCreateView.as_view(), name= 'movie-create'),
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name= 'movie-update'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name= 'movie-delete'),
    # path('movie_create', views.movie_create, name= 'movie_create'),
    path('movie_update/<int:id>/',  views.movie_update, name= 'movie_update'),
    # path('movie_delete/<int:id>/',  views.movie_delete, name= 'movie_delete'),
    # path('movie/<int:movie_id>/',  views.movie_detail, name='movie_detail'),
    path('upvote_movie/<int:movie_id>/',  views.movie_upvote, name='movie_upvote'),

    #Series
    path('series/', views.all_series, name= 'all_series'),
    path('create_serial', views.serial_create, name= 'serial_create'),
    path('update_serial/<int:id>/',  views.serial_update, name= 'serial_update'),
    path('delete_serial/<int:id>/',  views.serial_delete, name= 'serial_delete'),
    path('serial<int:serial_id>/',  views.serial_detail, name='serial_detail'),
    path('upvote_serial/<int:serial_id>/', views.serial_upvote, name='serial_upvote'),

    #Anime
    path('animes/', views.all_animes, name= 'all_animes'),
    path('anime_create', views.anime_create, name= 'anime_create'),
    path('anime_update/<int:id>/',  views.anime_update, name= 'anime_update'),
    path('anime_delete/<int:id>/',  views.anime_delete, name= 'anime_delete'),
    path('anime/<int:anime_id>/',  views.anime_detail, name='anime_detail'),
    path('anime_upvote/<int:anime_id>/',  views.anime_upvote, name='anime_upvote'),


    #Anime
    path('xvideos/', views.all_xvideos, name= 'all_xvideos'),
    path('xvideo_create', views.xvideo_create, name= 'xvideo_create'),
    path('xvideo_update/<int:id>/',  views.xvideo_update, name= 'xvideo_update'),
    path('xvideo_delete/<int:id>/',  views.xvideo_delete, name= 'xvideo_delete'),
    path('xvideo/<int:xvideo_id>/',  views.xvideo_detail, name='xvideo_detail'),
    path('xvideo_upvote/<int:xvideo_id>/',  views.xvideo_upvote, name='xvideo_upvote'),






]
