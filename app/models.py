from django.db import models

# Create your models here.


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    tell_phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
