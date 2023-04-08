from django.contrib import admin
from .models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status']
    list_editable = ['rating', 'year', 'budget']
    ordering = ['-rating', '-name']
    list_per_page = 10

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return "Лучше не смотреть!!!"
        if mov.rating < 70:
            return "Нормально"
        if mov.rating <= 85:
            return "Зачет"
        return "Топчик"
