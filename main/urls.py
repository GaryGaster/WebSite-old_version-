from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.all_movies, name= 'all_movies'),
    path('movie_create', views.movie_create, name= 'movie_create'),
    path('movie_update/<int:id>/',  views.movie_update, name= 'movie_update'),
    path('movie_delete/<int:id>/',  views.movie_delete, name= 'movie_delete'),
    path('movie/<int:movie_id>/',  views.movie_detail, name='movie_detail'),
    path('upvote_movie/<int:movie_id>/',  views.movie_upvote, name='movie_upvote'),

    #Series
    path('series/', views.all_series, name= 'all_series'),
    path('create_serial', views.serial_create, name= 'serial_create'),
    path('update_serial/<int:id>/',  views.serial_update, name= 'serial_update'),
    path('delete_serial/<int:id>/',  views.serial_delete, name= 'serial_delete'),
    path('serial<int:serial_id>/',  views.serial_detail, name='serial_detail'),
    path('upvote_serial/<int:serial_id>/', views.serial_upvote, name='serial_upvote'),

    #Anime
    path('anime/', views.all_animes, name= 'all_animes'),
    path('anime_create', views.anime_create, name= 'anime_create'),
    path('anime_update/<int:id>/',  views.anime_update, name= 'anime_update'),
    path('anime_delete/<int:id>/',  views.anime_delete, name= 'anime_delete'),
    path('anime/<int:anime_id>/',  views.anime_detail, name='anime_detail'),
    path('anime_upvote/<int:anime_id>/',  views.anime_upvote, name='anime_upvote'),
    #
    # #Xvideo
    # path('', views.all_movies, name= 'all_movies'),
    # path('create_movie', views.create_movie, name= 'create_movie'),
    # path('update_movie/<int:id>/',  views.update_movie, name= 'update_movie'),
    # path('delete_movie/<int:id>/',  views.delete_movie, name= 'delete_movie'),
    # path('<int:movie_id>/',  views.detail, name='detail'),
    # path('<int:movie_id>/upvote_xvideo/',  views.upvote_xvideo, name='upvote_xvideo'),
    #
    #



]
