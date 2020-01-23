from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm, VideoForm
from .models import Movie

def all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'main/all_movies.html', {'movies': movies})

def create_movie(request):
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
            return render(request, 'main/video_form.html', {'error': 'Tytuł oraz zdjęcie filmu są konieczne !'})
    else:
        return render(request, 'main/video_form.html', {'form': form})





def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if movie.user == request.user:
        if form.is_valid():
            movie.save()
            return redirect(all_movies)
        else:
            return render(request, 'main/video_form.html', {'form': form})

    else:
        return render(request, 'main/refusal.html')

def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if movie.user == request.user:
        if request.method == 'POST':
            movie.delete()
            return redirect(all_movies)
        return render(request, 'main/confirm.html', {'movie': movie})

    else:
        return render(request, 'main/refusal.html')

def upvote(request, movie_id):
    if request.method == "POST":
        product = get_object_or_404(Movie, pk=movie_id)
        if request.user not in product.voters.all():
            product.votes_total += 1
            product.voters.add(request.user)
            product.save()

        return redirect('all_movies')