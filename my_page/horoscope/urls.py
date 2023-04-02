from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:sign_of_zodiac>/', views.get_horoscope_by_num),
    path('<str:sign_of_zodiac>/', views.get_horoscope_by_sign, name='horoscope-name'),
    path('type/', views.type_sign),
    path('type/<str:type_name>/', views.type, name='types_names'),

]




