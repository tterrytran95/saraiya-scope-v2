from django.db import models

# Create your models here.
class Museum(models.Model):
    img_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')

class CurrentFrame(models.Model):
    img_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
    