from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField()
