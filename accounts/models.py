from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        db_table = "accounts_users"

    avatar = models.CharField(max_length=100)
