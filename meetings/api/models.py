from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Registry(models.Model):
    pass


class Group(models.Model):
    pass


class Meeting(models.Model):
    pass
