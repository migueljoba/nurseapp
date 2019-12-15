from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None

    is_nurse = models.BooleanField(default=False)
    is_patiente = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
        verbose_name_plural = 'users'
