from django.db import models

# Create your models here.
class ABOUT(models.Model):
    description = models.CharField(max_length=500)
    designation = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    birthday = models.DateField()
    website = models.URLField()
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()

class SOCIAL(models.Model):
    social_icon = models.CharField(max_length=100)
    social_link = models.URLField(max_length=1000)

    def __str__(self):
        return self.social_icon
    
class SERVICE(models.Model):
    service_icon = models.CharField(max_length=100)
    service_title = models.CharField(max_length=100)
    service_description = models.CharField(max_length=500)    
    image = models.ImageField(upload_to='SERVICE/', blank=True, null=True)
    
    def __str__(self):
        return self.service_title

class CONTACT(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    massege = models.CharField(max_length=1000)