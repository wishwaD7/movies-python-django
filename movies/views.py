from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie



def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Hello, Home. Welcome to Movies")