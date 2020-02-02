from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm, SerialForm, AnimeForm
from .models import Movie, Serial, Anime
from django.contrib.auth.decorators import login_required


#Filmy
def all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'main/all_movies.html', {'movies': movies})

@login_required
def movie_create(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.FILES['image']:
            movie = Movie()
            movie.title = request.POST['title']
            movie.description = request.POST['description']
            movie.year = request.POST['year']
            movie.image = request.FILES['image']
            movie.user = request.user
            movie.save()
            return redirect(all_movies)
        else:
            return render(request, 'main/movie_form.html', {'error': 'Tytuł oraz zdjęcie filmu są konieczne !'})
    else:
        return render(request, 'main/movie_form.html', {'form': form})




@login_required
def movie_update(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if movie.user == request.user:
        if form.is_valid():
            movie.save()
            return redirect(all_movies)
        else:
            return render(request, 'main/movie_form.html', {'form': form})

    else:
        return render(request, 'main/refusal.html')

@login_required
def movie_delete(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if movie.user == request.user:
        if request.method == 'POST':
            movie.delete()
            return redirect(all_movies)
        return render(request, 'main/movie_confirm.html', {'movie': movie})

    else:
        return render(request, 'main/refusal.html')

@login_required
def movie_upvote(request, movie_id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, pk=movie_id)
        if request.user not in movie.voters.all():
            movie.votes_total += 1
            movie.voters.add(request.user)
            movie.save()

        return redirect('all_movies')

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'main/movie_detail.html', {"movie":movie})


#Seriale
def all_series(request):
    series = Serial.objects.all()
    return render(request, 'main/all_series.html', {'series': series})

@login_required
def serial_create(request):
    form = SerialForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.FILES['image']:
            serial = Serial()
            serial.title = request.POST['title']
            serial.description = request.POST['description']
            serial.year = request.POST['year']
            serial.image = request.FILES['image']
            serial.user = request.user
            serial.save()
            return redirect(all_series)
        else:
            return render(request, 'main/serial_form.html', {'error': 'Tytuł oraz zdjęcie filmu są konieczne !'})
    else:
        return render(request, 'main/serial_form.html', {'form': form})




@login_required
def serial_update(request, id):
    serial = get_object_or_404(Serial, pk=id)
    form = SerialForm(request.POST or None, request.FILES or None, instance=serial)

    if serial.user == request.user:
        if form.is_valid():
            serial.save()
            return redirect(all_series)
        else:
            return render(request, 'main/serial_form.html', {'form': form})

    else:
        return render(request, 'main/refusal.html')

@login_required
def serial_delete(request, id):
    serial = get_object_or_404(Serial, pk=id)

    if serial.user == request.user:
        if request.method == 'POST':
            serial.delete()
            return redirect(all_series)
        return render(request, 'main/serial_confirm.html', {'serial': serial})

    else:
        return render(request, 'main/refusal.html')

@login_required
def serial_upvote(request, serial_id):
    if request.method == "POST":
        serial = get_object_or_404(Serial, pk=serial_id)
        if request.user not in serial.voters.all():
            serial.votes_total += 1
            serial.voters.add(request.user)
            serial.save()

        return redirect('all_series')

def serial_detail(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    return render(request, 'main/serial_detail.html', {"serial":serial})


#Anime
def all_animes(request):
    animes = Anime.objects.all()
    return render(request, 'main/all_animes.html', {'animes': animes})

@login_required
def anime_create(request):
    form = AnimeForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.FILES['image']:
            anime = Anime()
            anime.title = request.POST['title']
            anime.description = request.POST['description']
            anime.year = request.POST['year']
            anime.image = request.FILES['image']
            anime.user = request.user
            anime.save()
            return redirect(all_animes)
        else:
            return render(request, 'main/anime_form.html', {'error': 'Tytuł oraz zdjęcie filmu są konieczne !'})
    else:
        return render(request, 'main/anime_form.html', {'form': form})




@login_required
def anime_update(request, id):
    anime = get_object_or_404(Anime, pk=id)
    form = AnimeForm(request.POST or None, request.FILES or None, instance=anime)

    if anime.user == request.user:
        if form.is_valid():
            anime.save()
            return redirect(all_animes)
        else:
            return render(request, 'main/anime_form.html', {'form': form})

    else:
        return render(request, 'main/refusal.html')

@login_required
def anime_delete(request, id):
    anime = get_object_or_404(Anime, pk=id)

    if anime.user == request.user:
        if request.method == 'POST':
            anime.delete()
            return redirect(all_animes)
        return render(request, 'main/anime_confirm.html', {'anime': anime})

    else:
        return render(request, 'main/refusal.html')

@login_required
def anime_upvote(request, anime_id):
    if request.method == "POST":
        anime = get_object_or_404(Anime, pk=anime_id)
        if request.user not in anime.voters.all():
            anime.votes_total += 1
            anime.voters.add(request.user)
            anime.save()

        return redirect('all_animes')

def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    return render(request, 'main/anime_detail.html', {"anime":anime})


