from django.urls import path

# from django.conf.url import url

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
