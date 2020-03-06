from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    avatar = models.ImageField()

    class Meta:
        db_table = 'users'
