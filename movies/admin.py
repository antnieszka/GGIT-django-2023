from django.contrib import admin

# Register your models here.
from movies.models import Movie, Director

admin.site.register(Movie)
admin.site.register(Director)
