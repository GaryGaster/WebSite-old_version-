from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name= 'home'),

    #Movies
    path('movies/', views.MovieListView.as_view(), name= 'movies-home'),
    path('movies/user/<str:username>', views.UserMovieListView.as_view(), name= 'user-movies'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name= 'movie-detail'),
    path('movies/new/', views.MovieCreateView.as_view(), name= 'movie-create'),
    path('movies/<int:pk>/update/', views.MovieUpdateView.as_view(), name= 'movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name= 'movie-delete'),
    path('upvote_movie/<int:movie_id>/',  views.movie_upvote, name='movie-upvote'),

    #Series
    path('series/', views.SerialListView.as_view(), name= 'series-home'),
    path('series/user/<str:username>', views.UserSerialListView.as_view(), name= 'user-series'),
    path('series/<int:pk>/', views.SerialDetailView.as_view(), name= 'serial-detail'),
    path('series/new/', views.SerialCreateView.as_view(), name= 'serial-create'),
    path('series/<int:pk>/update/', views.SerialUpdateView.as_view(), name= 'serial-update'),
    path('series/<int:pk>/delete/', views.SerialDeleteView.as_view(), name= 'serial-delete'),
    path('upvote_serial/<int:serial_id>/',  views.serial_upvote, name='serial-upvote'),

    #Animes    
    path('animes/', views.AnimeListView.as_view(), name= 'animes-home'),
    path('animes/user/<str:username>', views.UserAnimeListView.as_view(), name= 'user-animes'),
    path('animes/<int:pk>/', views.AnimeDetailView.as_view(), name= 'anime-detail'),
    path('animes/new/', views.AnimeCreateView.as_view(), name= 'anime-create'),
    path('animes/<int:pk>/update/', views.AnimeUpdateView.as_view(), name= 'anime-update'),
    path('animes/<int:pk>/delete/', views.AnimeDeleteView.as_view(), name= 'anime-delete'),
    path('upvote_anime/<int:anime_id>/',  views.anime_upvote, name='anime-upvote'),

    # Xvideos
    path('xvideos/verify_user_age/', views.verify_age, name= 'verify-age'),
    path('xvideos/', views.XvideoListView.as_view(), name='xvideos-home'),
    path('xvideos/user/<str:username>', views.UserXvideoListView.as_view(), name='user-xvideos'),
    path('xvideos/<int:pk>/', views.XvideoDetailView.as_view(), name='xvideo-detail'),
    path('xvideos/new/', views.XvideoCreateView.as_view(), name='xvideo-create'),
    path('xvideos/<int:pk>/update/', views.XvideoUpdateView.as_view(), name='xvideo-update'),
    path('xvideos/<int:pk>/delete/', views.XvideoDeleteView.as_view(), name='xvideo-delete'),
    path('upvote_xvideo/<int:xvideo_id>/', views.xvideo_upvote, name='xvideo-upvote'),





]