from django.shortcuts import render
from .models import ABOUT

# Create your views here.
def Index(request):
    # social = SOCIAL.objects.all()
    return render(request, 'index.html')

def About(request):
    about = ABOUT.objects.get()
    return render(request, 'about.html', {'about':about})