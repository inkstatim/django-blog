from django.urls import path
from . import views
urlpatterns = [
    path('load_img', views.CreateGalleryView.as_view()),
    path('list_img', views.ListGallery.as_view())
]