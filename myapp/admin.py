from django.contrib import admin
from .models import ABOUT, SOCIAL, SERVICE, CONTACT

# Register your models here.
admin.site.register(ABOUT)     
admin.site.register(SOCIAL)
admin.site.register(SERVICE)
admin.site.register(CONTACT)
