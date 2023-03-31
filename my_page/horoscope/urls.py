from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('<int:sign_of_zodiac>/', views.get_horoscope_by_num),
    path('<str:sign_of_zodiac>/', views.get_horoscope_by_sign, name = 'horoscope-name')
]
