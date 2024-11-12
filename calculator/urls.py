from django.urls import path
from .views import calculate, index

urlpatterns = [
    path('', index, name='index'),
    path('calculate/', calculate, name='calculate'),
]