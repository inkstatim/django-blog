from django.urls import path
from . import views
urlpatterns = [
    path('list', views.ListFeedBack.as_view()),
    path('detail/<id_feedback>', views.DetailFeedBack.as_view()),
    path('done', views.DoneView.as_view()),
    path('', views.FeedbackView.as_view()),
    path('<id_feed>', views.UpdateFeedbackView.as_view()),

]
