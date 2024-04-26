from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    chat_id = models.CharField(max_length=250, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
