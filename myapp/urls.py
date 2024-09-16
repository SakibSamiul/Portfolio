from django.urls import path
from . views import Index, About

urlpatterns = [
    path('', Index, name= 'index'),
    path('about', About, name= 'about'),
]
