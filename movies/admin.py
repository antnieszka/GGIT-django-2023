from django.contrib import admin

# Register your models here.
from movies.models import Movie

admin.site.register(Movie)
