from django.urls import path
from . views import Index, About, Resume

urlpatterns = [
    path('', Index, name= 'index'),
    path('about', About, name= 'about'),
    path('resume', Resume, name = 'resume'),
]
