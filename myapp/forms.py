from django import forms
from .models import *

class CONTACTFORM(forms.ModelForm):
    class Meta:
        model = CONTACT
        fields = {'name', 'email', 'subject', 'massege'}