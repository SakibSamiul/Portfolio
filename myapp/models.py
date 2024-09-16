from django.db import models

# Create your models here.
class ABOUT(models.Model):
    description = models.CharField(max_length=500)
    designation = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    birthday = models.DateField()
    website = models.URLField()
    phone = models.IntegerField(max_length=15)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()

class SOCIAL(models.Model):
    social_icon = models.CharField(max_length=100)
    social_link = models.URLField(max_length=1000)

    def __str__(self):
        return self.social_icon