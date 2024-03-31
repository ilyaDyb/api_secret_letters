from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    api_key = models.CharField(max_length=200)

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username
