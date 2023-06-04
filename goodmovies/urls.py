"""
URL configuration for goodmovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.hello_world, name="hello"),
    path("filmy/", views.MovieList.as_view(), name="movies_list"),
    path("filmy/create/", views.MovieCreate.as_view(), name="movies_create"),
    path("filmy/<int:pk>/", views.MovieDetail.as_view(), name="movies_detail"),
    path("filmy/<int:pk>/update/", views.MovieUpdate.as_view(), name="movies_update"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.profile_view, name="user_profile"),
    path("accounts/signup/", views.user_signup, name="user_signup"),
]
