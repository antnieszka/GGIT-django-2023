from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    published_at = models.DateTimeField()
    rating = models.IntegerField()
    director = models.ForeignKey(
        to="movies.Director",
        on_delete=models.CASCADE,
        verbose_name="reżyser",
        related_name="movies",
        null=True,
    )

    class Meta:
        verbose_name = "film"
        verbose_name_plural = "filmy"

    def __str__(self):
        return self.title


class Director(models.Model):
    first_name = models.CharField(verbose_name="imię", max_length=100)
    last_name = models.CharField(verbose_name="nazwisko", max_length=100)
    about = models.TextField(verbose_name="opis", blank=True)

    class Meta:
        verbose_name = "reżyser"
        verbose_name_plural = "reżyserzy"

    def __str__(self):
        return "Reżyser: " + self.first_name + " " + self.last_name
