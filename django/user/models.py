from django.db import models

# Create your models here.

class Admin(models.Model):
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(null=False, max_length=50)
