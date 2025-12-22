from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('customer', 'Customer')
    ]
    email=models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default='customer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} is {self.role}'
