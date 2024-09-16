from django.urls import path
from . views import Index, About, Resume, Services, Service_details, Portfolio, Portfolio_details, Contact

urlpatterns = [
    path('', Index, name= 'index'),
    path('about', About, name= 'about'),
    path('resume', Resume, name= 'resume'),
    path('services', Services, name= 'services'),
    path('service-details/<int:pk>/', Service_details, name= 'service_details'),
    path('portfolio', Portfolio, name= 'portfolio'),
    path('portfolio-details', Portfolio_details, name= 'portfolio-details'),
    path('contact', Contact, name= 'contact'),
]
