from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    # Movies
    path('movies/', views.MovieListView.as_view(), name='movies-home'),
    path('movies/user/<str:username>', views.UserMovieListView.as_view(), name='user-movies'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/new/', views.MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('upvote_movie/<int:movie_id>/', views.movie_upvote, name='movie-upvote'),

    # Series
    path('series/', views.SerialListView.as_view(), name='series-home'),
    path('series/user/<str:username>', views.UserSerialListView.as_view(), name='user-series'),
    path('series/<int:pk>/', views.SerialDetailView.as_view(), name='serial-detail'),
    path('series/new/', views.SerialCreateView.as_view(), name='serial-create'),
    path('series/<int:pk>/update/', views.SerialUpdateView.as_view(), name='serial-update'),
    path('series/<int:pk>/delete/', views.SerialDeleteView.as_view(), name='serial-delete'),
    path('upvote_serial/<int:serial_id>/', views.serial_upvote, name='serial-upvote'),

    # Anime
    path('anime/', views.AnimeListView.as_view(), name='anime-home'),
    path('anime/user/<str:username>', views.UserAnimeListView.as_view(), name='user-anime'),
    path('anime/<int:pk>/', views.AnimeDetailView.as_view(), name='anime-detail'),
    path('anime/new/', views.AnimeCreateView.as_view(), name='anime-create'),
    path('anime/<int:pk>/update/', views.AnimeUpdateView.as_view(), name='anime-update'),
    path('anime/<int:pk>/delete/', views.AnimeDeleteView.as_view(), name='anime-delete'),
    path('upvote_anime/<int:anime_id>/', views.anime_upvote, name='anime-upvote'),

]
