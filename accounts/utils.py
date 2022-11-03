import csv
import os
import re
from typing import Iterable

import xml.etree.ElementTree as ET

from accounts.validators import UserValidation


class Parser:
    def __init__(self, xml_file: object, csv_file: Iterable[str]):
        self.xml_file = xml_file
        self.csv_file = csv_file

    def parse_csv(self):
        reader = csv.reader(self.csv_file)
        user_data_1 = []
        for row in reader:
            user_data_1.append(
                {"username": row[0], "password": row[1], "date_joined": row[2]}
            )
        self.csv_file.close()
        try:
            os.remove("./accounts/downloads/csv_file.csv")
        except:
            pass
        return user_data_1

    def parse_xml(self):
        root = ET.parse(self.xml_file).getroot()
        user_data_2 = []
        for user in root.find("user").find("users").findall("user"):
            user_data_2.append(
                {
                    "first_name": user.find("first_name").text,
                    "last_name": user.find("last_name").text,
                    "avatar": user.find("avatar").text,
                    "id": user.attrib.get("id"),
                }
            )
        return user_data_2


class DataValidator:
    def __init__(self, user_data_1: list, user_data_2: list):
        self.user_data_1 = user_data_1
        self.user_data_2 = user_data_2

    def remove_invalid_data(self):
        list_data = [self.user_data_1, self.user_data_2]
        for users_data in list_data:
            for user in users_data:
                for key, data_ in user.items():
                    if data_:
                        user[key] = (
                            "".join(re.split(r"\(.*\)", data_)[::])
                            .removesuffix(" ")
                            .removeprefix(" ")
                        )
        return self.user_data_1, self.user_data_2

    def merge_user_info(self):
        self.remove_invalid_data()
        data = []
        del self.user_data_1[0]
        for user_data_1 in self.user_data_1:
            for user_data_2 in self.user_data_2:
                if (
                    user_data_2.get("first_name")
                    and len(user_data_2.get("first_name")) > 0
                ):
                    created_username = (
                        user_data_2.get("first_name")[0]
                        + "."
                        + user_data_2.get("last_name")
                        if type(user_data_2.get("last_name")) == str
                        else ""
                    )
                    if user_data_1.get("username").upper() == created_username.upper():
                        data.append({**user_data_1, **user_data_2})
        return data

    def validate_user_info(self):
        data = self.merge_user_info()
        users = []
        for user in data:
            try:
                UserValidation(**user)
            except:
                continue
            users.append(user)
        return users
