import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = "accounts_users"

    avatar = models.TextField(null=True, default=None)

    @staticmethod
    def create_users_objects_from_list(users: list[dict]):
        return [
            User(
                username=user.get("username"),
                first_name=user.get("first_name"),
                last_name=user.get("last_name"),
                password=make_password(user.get("password")),
                date_joined=datetime.date.fromtimestamp(int(user.get("date_joined"))),
                id=user.get("id"),
                avatar=user.get("avatar"),
            )
            for user in users
        ]
