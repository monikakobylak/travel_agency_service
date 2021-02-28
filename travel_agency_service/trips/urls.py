from django.urls import path
from . import views

app_name = 'trips'


urlpatterns = [
    path('main/', views.main, name='main'),
]
