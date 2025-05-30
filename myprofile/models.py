# profileapp/models.py
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    extra = models.TextField(blank=True)

    def __str__(self):
        return self.name
