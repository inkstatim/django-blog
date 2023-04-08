from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return (
            ('<40', 'Низкий'),
            ('40-60', 'Средний'),
            ('60-80', 'Высокий'),
            ('>80', 'Самый высокий'),
        )

    def queryset(self, request, queryset: QuerySet):
        rating = self.value()  # или request.GET.get('rating')
        match rating:
            case '<40':
                return queryset.filter(rating__lt=40)
            case '40-60':
                return queryset.filter(rating__gte=40, rating__lte=60)
            case '60-80':
                return queryset.filter(rating__gte=60, rating__lte=80)
            case '>80':
                return queryset.filter(rating__gt=80)


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'budget', 'currency']
    ordering = ['-rating', '-name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euros']
    search_fields = ['name', 'rating']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return "Лучше не смотреть!!!"
        if mov.rating < 70:
            return "Нормально"
        if mov.rating <= 85:
            return "Зачет"
        return "Топчик"

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euros(self, request, qs: QuerySet):
        qs.update(currency=Movie.EUR)
