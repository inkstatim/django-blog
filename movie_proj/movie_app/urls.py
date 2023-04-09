from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.ddirectors),
    path('directors/<slug:slug_name>', views.name_director, name='dir-detail'),
    path('actors', views.info_actors),
    path('actors/<int:id_act>', views.info_actor, name='actor-detail'),

]
