from django.urls import path
from . import views

app_name = 'calculator_app'

urlpatterns = [
    path('', views.calculate, name='calculate'),
    
]
