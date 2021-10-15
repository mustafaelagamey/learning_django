from django.db import models


# Create your models here.
class Feedback(models.Model):
    user_name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
