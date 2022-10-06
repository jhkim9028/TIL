
from django.shortcuts import redirect, render
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

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request,'movie/edit.html',context)

def create(request):
    
    title = request.GET.get('title_')
    summary = request.GET.get('summary_')
    running_time = request.GET.get('running_')
    Movie.objects.create(title=title, summary=summary,running_time=running_time)
    
    return redirect('movie:index')

def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('movie:index')

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    title = request.GET.get('title_')
    summary = request.GET.get('summary_')
    running_time = request.GET.get('running_')
    
    movie.title = title
    movie.summary = summary
    movie.running_time = running_time
    
    movie.save()
    return redirect('movie:detail', movie.pk)