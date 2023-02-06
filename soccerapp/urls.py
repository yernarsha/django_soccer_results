from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="home"),
    path('today', views.today, name="today"),
]