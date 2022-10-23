from enum import unique
from django.db import models

# Create your models here.
class Order(models.Model):
    email = models.EmailField(max_length=1000,unique=True)
    order=models.CharField(max_length=30)
    quantity=models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']