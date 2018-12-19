from django.urls import path

from . import views

urlpatterns = [
    path('', views.cover, name='cover'),
    path('home/', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
]
