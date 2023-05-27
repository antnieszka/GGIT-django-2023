from django.shortcuts import render
from datetime import datetime

from movies.models import Movie


def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(request, template_name="hello.html", context=our_context)


def list_movies(request):
    movies = Movie.objects.all()
    return render(request, template_name="movie_list.html", context={"movies": movies})


def profile_view(request):
    return render(request, template_name="registration/profile.html")
