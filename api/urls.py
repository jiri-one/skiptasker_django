from django.urls import path
from .views import TasksAPI, OneTaskAPI

urlpatterns = [
    path("", TasksAPI.as_view()),
    path("create/", TasksAPI.as_view()),
    path("update/<int:id>/", TasksAPI.as_view()),
    path("<int:id>/", OneTaskAPI.as_view()),
]
