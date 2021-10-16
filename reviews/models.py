from django.db import models

# Create your models here.
from django.urls import reverse


class Feedback(models.Model):
    user_name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()

    def get_absolute_url(self):
        return reverse('reviews:feedback-detail', args=[self.id])
