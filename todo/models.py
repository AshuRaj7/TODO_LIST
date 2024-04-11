from django.db import models

class data(models.Model):
    title= models.CharField(max_length=10000)
    def __str__(self):
        return self.title
# Create your models here.
