from django.db import models
from users.models import User

class Letters(models.Model):
    letter_id = models.CharField(max_length=300, primary_key=True, null=False)
    text = models.TextField(null=False)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "Letters"

