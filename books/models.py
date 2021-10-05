from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Address(models.Model):
    street = models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return self.full_address()

    def full_address(self):
        return f"{self.city} , {self.street}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(5)
        ])
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("books:detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super().save(args, kwargs)
