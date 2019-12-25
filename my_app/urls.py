from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #it will display data from views.home
]
