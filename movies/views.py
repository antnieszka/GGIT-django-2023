from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
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


from django.contrib.auth.forms import UserCreationForm


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
