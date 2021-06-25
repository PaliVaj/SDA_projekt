from django.urls import path

from weather_api import views

app_name = 'weather_api'

urlpatterns = [
    path('weather', views.weather, name='weather'),

]