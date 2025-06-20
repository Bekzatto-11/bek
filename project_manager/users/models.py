from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    position = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username
