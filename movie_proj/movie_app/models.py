from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"{self.floor}  {self.number}"


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Director, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('dir-detail', args=[self.slug])


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актер {self.first_name} {self.last_name}"
        else:
            return f"Актриса {self.first_name} {self.last_name}"

    def get_url(self):
        return reverse('actor-detail', args=[self.id])


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
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}"
