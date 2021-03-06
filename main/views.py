from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .form import MovieForm, SerialForm, AnimeForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Movie, Serial, Anime


# Home
def home(request):
    movies = Movie.objects.all()
    return render(request, 'main/home.html', {'movies': movies})


# Movie
@login_required
def movie_upvote(request, movie_id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, pk=movie_id)
        if request.user not in movie.voters.all():
            movie.votes_total += 1
            movie.voters.add(request.user)
            movie.save()
            return redirect('movies-home')
        else:
            movie.votes_total -= 1
            movie.voters.remove(request.user)
            movie.save()
            return redirect('movies-home')


class UserMovieListView(ListView):
    model = Movie
    template_name = 'main/user_movies.html'
    context_object_name = 'movies'
    ordering = ['-timestamp']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Movie.objects.filter(user=user).order_by('-timestamp')


class MovieListView(ListView):
    model = Movie
    template_name = 'main/movies_home.html'
    context_object_name = 'movies'
    ordering = ['-timestamp']
    paginate_by = 12


class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.user:
            return True
        return False


class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    success_url = '/movies/'

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.user:
            return True
        return False


# Series

@login_required
def serial_upvote(request, serial_id):
    if request.method == "POST":
        serial = get_object_or_404(Serial, pk=serial_id)
        if request.user not in serial.voters.all():
            serial.votes_total += 1
            serial.voters.add(request.user)
            serial.save()
            return redirect('series-home')
        else:
            serial.votes_total -= 1
            serial.voters.remove(request.user)
            serial.save()
            return redirect('series-home')


class UserSerialListView(ListView):
    model = Serial
    template_name = 'main/user_series.html'
    context_object_name = 'series'
    ordering = ['-timestamp']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Serial.objects.filter(user=user).order_by('-timestamp')


class SerialListView(ListView):
    model = Serial
    template_name = 'main/series_home.html'
    context_object_name = 'series'
    ordering = ['-timestamp']
    paginate_by = 15


class SerialDetailView(DetailView):
    model = Serial


class SerialCreateView(LoginRequiredMixin, CreateView):
    model = Serial
    form_class = SerialForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SerialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Serial
    form_class = SerialForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        serial = self.get_object()
        if self.request.user == serial.user:
            return True
        return False


class SerialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Serial
    success_url = '/series/'

    def test_func(self):
        serial = self.get_object()
        if self.request.user == serial.user:
            return True
        return False


# Anime


@login_required
def anime_upvote(request, anime_id):
    if request.method == "POST":
        anime = get_object_or_404(Anime, pk=anime_id)
        if request.user not in anime.voters.all():
            anime.votes_total += 1
            anime.voters.add(request.user)
            anime.save()
            return redirect('anime-home')
        else:
            anime.votes_total -= 1
            anime.voters.remove(request.user)
            anime.save()
            return redirect('anime-home')


class UserAnimeListView(ListView):
    model = Anime
    template_name = 'main/user_anime.html'
    context_object_name = 'anime'
    ordering = ['-timestamp']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Anime.objects.filter(user=user).order_by('-timestamp')


class AnimeListView(ListView):
    model = Anime
    template_name = 'main/anime_home.html'
    context_object_name = 'anime'
    ordering = ['-timestamp']
    paginate_by = 15


class AnimeDetailView(DetailView):
    model = Anime


class AnimeCreateView(LoginRequiredMixin, CreateView):
    model = Anime
    form_class = AnimeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnimeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Anime
    form_class = AnimeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        anime = self.get_object()
        if self.request.user == anime.user:
            return True
        return False


class AnimeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Anime
    success_url = '/anime/'

    def test_func(self):
        anime = self.get_object()
        if self.request.user == anime.user:
            return True
        return False
