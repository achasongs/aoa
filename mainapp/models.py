from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

