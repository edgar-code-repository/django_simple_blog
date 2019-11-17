from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    full_name = models.CharField(max_length=180)

    class Meta:
        ordering = ["last_name"]
    
    def __str__(self):
        return "[User: " + self.username + " - Email: " + self.email + "]"


class Technology(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name


class Category(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField()

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=250)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["-last_modification_date", "-publication_date"]
    
    def __str__(self):
        return self.title
