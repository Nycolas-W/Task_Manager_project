from django.urls import path
from . import views
from .views import task_list

urlpatterns = [
    path('', task_list, name = 'task_list'),
    path('',views.task_list, name='task_list'),
    path('add/', views.add_task, name = 'add_task'),
]