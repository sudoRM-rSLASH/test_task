import csv
import xml.etree.ElementTree as ET


class Parser(object):
    def __init__(self, xml_file, csv_file):
        self.xml_file = xml_file,
        self.csv_file = csv_file

    def parse_csv(self):
        reader = csv.reader(self.csv_file)
        data = []
        user = {}
        for row in reader:
            user['username'] = row[0]
            user['password'] = row[1]
            user['date_joined'] = row[2]
            data.append(user)
        return data

    def parse_xml(self):
        tree = ET.parse(self.csv_file)
        root = tree.getroot()
        data_ = []
        user_ = {}
        for user in root.find('user').find('users').findall('user'):
            user_['first_name'] = user.find('first_name').text
            user_['last_name'] = user.find('last_name').text
            user_['avatar'] = user.find('avatar').text
            data_.append(user_)
        return data_
