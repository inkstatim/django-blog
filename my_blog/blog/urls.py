from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('posts/<int:num>/', views.get_info_about_num),
    path('posts/<str:name_post>/', views.get_posts),
]
