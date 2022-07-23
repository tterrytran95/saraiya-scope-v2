from django.db import models

# Create your models here.
class Museum(models.Model):
    img_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')

class CurrentFrame(models.Model):
    img_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
    
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    
    
class TerrysModel(models.Model):
    name = models.CharField(max_length = 200)
    index = models.IntegerField()
    
    def __str__(self):
        return self.name
    