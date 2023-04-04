from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - { self.rating}%"
