from django.db import models

# Create your models here.

class Games(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Games')
    price = models.IntegerField(default=60)


    def __str__(self):
        return self.title