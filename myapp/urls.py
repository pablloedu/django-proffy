from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('study/', views.study, name='study'),
    path('studyFilter/', views.studyFilter, name='studyFilter'),
    path('give-classes/', views.giveClasses, name='give-classes'),

]