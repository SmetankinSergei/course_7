from django.contrib.auth.models import AbstractUser


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    pass
