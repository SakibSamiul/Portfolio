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


