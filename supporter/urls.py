from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('diary', views.diary, name='diary'),
    path('contrib_calc', views.contrib_calc, name='contrib_calc'),
    path('tasks', views.tasks, name='tasks'),
]
