from django.db import models
from django.contrib.auth.models import AbstractUser

class Coach(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
