from django.shortcuts import render, redirect
from .models import ABOUT, SOCIAL, SERVICE
from .forms import *
# Create your views here.
def Index(request):
    social = SOCIAL.objects.all()
    return render(request, 'index.html', {'social':social})

def About(request):
    about = ABOUT.objects.get()
    return render(request, 'about.html', {'about':about})

def Resume(request):
    return render(request, 'resume.html')

def Services(request):
    service = SERVICE.objects.all()
    return render(request, 'services.html', {'service':service})

def Service_details(request, pk):
    service_details = SERVICE.objects.get(pk=pk)
    return render(request, 'service-details.html', { 'service_details':service_details})

def Portfolio(request):
    return render(request, 'portfolio.html')

def Portfolio_details(request):
    return render(request, 'portfolio-details.html')

def Contact(request):
    form = CONTACTFORM(request.POST)
    if request.method == 'POST':
        form = CONTACTFORM(request.POST)
        if form .is_valid():
            form.save()
            return redirect('index')
        
    return render(request, 'contact.html', {'form':form})
