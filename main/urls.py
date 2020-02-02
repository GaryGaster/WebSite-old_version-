from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.all_movies, name= 'all_movies'),
    path('create_movie', views.create_movie, name= 'create_movie'),
    path('update_movie/<int:id>/',  views.update_movie, name= 'update_movie'),
    path('delete_movie/<int:id>/',  views.delete_movie, name= 'delete_movie'),
    path('movie/<int:movie_id>/',  views.detail_movie, name='detail_movie'),
    path('upvote_movie/<int:movie_id>/',  views.upvote_movie, name='upvote_movie'),

    #Series
    path('series/', views.all_series, name= 'all_series'),
    path('create_serial', views.create_serial, name= 'create_serial'),
    path('update_serial/<int:id>/',  views.update_serial, name= 'update_serial'),
    path('delete_serial/<int:id>/',  views.delete_serial, name= 'delete_serial'),
    path('serial<int:serial_id>/',  views.detail_serial, name='detail_serial'),
    path('upvote_serial/<int:serial_id>/', views.upvote_serial, name='upvote_serial'),

    # #Anime
    # path('', views.all_movies, name= 'all_movies'),
    # path('create_movie', views.create_movie, name= 'create_movie'),
    # path('update_movie/<int:id>/',  views.update_movie, name= 'update_movie'),
    # path('delete_movie/<int:id>/',  views.delete_movie, name= 'delete_movie'),
    # path('<int:movie_id>/',  views.detail, name='detail'),
    # path('<int:movie_id>/upvote_anime/',  views.upvote_anime, name='upvote_anime'),
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
