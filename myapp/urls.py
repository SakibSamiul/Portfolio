from django.urls import path
from . views import Index, About, Resume, Services, Service_details

urlpatterns = [
    path('', Index, name= 'index'),
    path('about', About, name= 'about'),
    path('resume', Resume, name = 'resume'),
    path('services', Services, name='services'),
    path('service-details', Service_details, name='service_details'),
]
