from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    USERNAME_FIELD = "email" #login with email
    REQUIRED_FIELDS = ['username'] 

    class Meta:
        verbose_name_plural = 'Usuários'

    def __str__(self):

        return self.username

