from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from movies.models import Movie


def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(request, template_name="hello.html", context=our_context)


def list_movies(request):
    movies = Movie.objects.all()
    return render(request, template_name="movie_list.html", context={"movies": movies})


def profile_view(request):
    return render(request, template_name="registration/profile.html")


def user_signup(request):
    context = {}
    if request.method == "POST":
        print("tworzymy uzytkownika")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                template_name="registration/singup_complete.html",
            )
        context["form"] = form
    else:
        print("wyswietlamy czysty formularz")
        context["form"] = UserCreationForm()

    return render(
        request,
        template_name="registration/singup_form.html",
        context=context,
    )


class MovieList(ListView):
    model = Movie
    # template_name = "movies/movie_list.html"
    # context_object_name = "movie_list"


class MovieDetail(DetailView):
    model = Movie
    # context_object_name = "movie"


class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ("title", "short_description")
    # template_name = "movies/movie_update.html"
    extra_context = {"title": "Edycja filmu"}

    def get_success_url(self):
        return reverse("movies_detail", args=[self.object.pk])


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ("title", "short_description", "published_at", "rating")
    # template_name = "movies/movie_create.html"
    extra_context = {"title": "Dodawanie nowego filmu"}

    def get_success_url(self):
        return reverse("movies_detail", args=[self.object.pk])
