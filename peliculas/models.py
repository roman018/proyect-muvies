from django.db import models
from django.utils import timezone


class peliculas(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sinopsis = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    action = "action"
    comedy = "comedy"
    horror = "horror"
    cartoon = "cartoon"
    family = "family"
    gender = [
        (action, "action"),
        (comedy, "comedy"),
        (horror, "horror"),
        (cartoon, "cartoon"),
        (family, "family")
    ]
    gender = models.CharField(
        max_length=20,
        choices = gender
    ) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name