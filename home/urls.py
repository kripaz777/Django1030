from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('category', category, name='category'),
    path('single', single, name='single'),
    path('contact', contact, name='contact'),
]