from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=80)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(5)
        ])

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("books:detail", args=[self.id])
