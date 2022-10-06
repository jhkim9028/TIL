from django.shortcuts import redirect, render
from movie.forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    
    context = {
        'movies':movies
    }
    return render(request, 'movie/index.html',context)

def new(request):
    return render(request, 'movie/new.html')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movie/detail.html',context)

def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movie:index')
    else:
        movie_form = MovieForm()
    context = {
        'movie_form': movie_form,
    }
    return render(request,'movie/new.html',context)
    
def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('movie:index')

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie.save()
            return redirect('movie:detail', movie.pk)
    else:
        movie_form = MovieForm(instance=movie)
    context = {
        'movie_form':movie_form,
    }
    return render(request,'movie/update.html',context)