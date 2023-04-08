from django.db import models
from django.urls import reverse
from django.utils.text import slugify
class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    UAH = 'UAH'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (UAH, 'Hrivnya'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=100000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=UAH)
    slug = models.SlugField(default='', null=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}"
