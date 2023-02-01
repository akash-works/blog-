from django.db import models


# Create your models here.

class User(models.Model):
    name  = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField( max_length=254)
    phone = models.CharField(max_length=12,null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name