from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #it will display data from views.home
    path('new_search', views.new_search, name="new_search"),
]
