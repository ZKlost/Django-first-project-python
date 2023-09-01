from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username