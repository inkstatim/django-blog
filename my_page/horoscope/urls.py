from django.urls import path
from . import views
urlpatterns = [
    path('<sign_of_zodiac>/', views.get_horoscope_by_sign)
]
