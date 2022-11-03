import re

from pydantic import BaseModel, validator


class UserValidation(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    date_joined: str
    avatar: str

    @validator("first_name", "last_name")
    def name_valid(cls, name):
        if not all(map(str.isalpha, name)):
            raise ValueError("incorrect First Name or Last Name")
        return name

    @validator("username")
    def username_valid(cls, username):
        if not all(
                map(lambda x: str.isalpha, username)
        ):
            raise ValueError("incorrect username")
        return username

    @validator("password")
    def password_valid(cls, password):
        if password:
            return password
        raise ValueError("Password must contain Upper symbol, and any number")


    @validator("date_joined")
    def date_joined_valid(cls, date_joined):
        if not date_joined:
            raise ValueError("Password must contain Upper symbol, and any number")
        return date_joined

    @validator("avatar")
    def avatar_valid(cls, avatar):
        if not avatar:
            raise ValueError("Password must contain Upper symbol, and any number")
        return avatar
