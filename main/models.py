from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    full_name = models.CharField(max_length=180)

    class Meta:
        ordering = ["last_name"]
    
    def __str__(self):
        return "[User: " + self.username + " - Email: " + self.email + "]"


