from django.test import TestCase

from accounts.utils import Parser, DataValidator

expected_data = [
    {
        "username": "M.Steam",
        "password": "ASDf43f#$dsD",
        "date_joined": "1638700932",
        "first_name": "Max",
        "last_name": "Steam",
        "avatar": "https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg",
        "id": "6",
    },
    {
        "username": "V.Markus",
        "password": "DSA4FSFF54w%$#df",
        "date_joined": "1464014817",
        "first_name": "Valeria",
        "last_name": "Markus",
        "avatar": "https://live.staticflickr.com/5252/5403292396_0804de9bcf_b.jpg",
        "id": "23",
    },
    {
        "username": "M.Stone",
        "password": "Lkds(*dsdadf",
        "date_joined": "1466078973",
        "first_name": "McMarry",
        "last_name": "Stone",
        "avatar": "https://photos.lensculture.com/large/5dd2fa6e-fe8d-469f-959b-46299ced511d.jpg",
        "id": "10",
    },
    {
        "username": "A.Mecman",
        "password": "MKds#$DSd",
        "date_joined": "1437646911",
        "first_name": "Anton",
        "last_name": "Mecman",
        "avatar": "https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/506829/original/Photo_on_2009-09-20_at_18.23_4/make-funny-faces-and-random-noises-to-random-people.jpg",
        "id": "85",
    },
    {
        "username": "A.Mechailov",
        "password": "35050Dsa",
        "date_joined": "1587145969",
        "first_name": "Anton",
        "last_name": "Mechailov",
        "avatar": "https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/35af6a41332353.57a1ce913e889.jpg",
        "id": "1",
    },
    {
        "username": "V.Jmishenko",
        "password": "MDsa4wtwefS",
        "date_joined": "1391924984",
        "first_name": "Valerii",
        "last_name": "Jmishenko",
        "avatar": "https://static.boredpanda.com/blog/wp-content/uploads/2017/04/Virrappan2-58f79980ae6fb__880.jpg",
        "id": "54",
    },
    {
        "username": "W.Terman",
        "password": "dSDr4wfDSD",
        "date_joined": "1484526287",
        "first_name": "Will",
        "last_name": "Terman",
        "avatar": "https://i.pinimg.com/736x/e6/09/16/e609168f9d1daec1b16be6a1832a2dd7.jpg",
        "id": "123",
    },
    {
        "username": "K.hex",
        "password": "mkSArwefd",
        "date_joined": "1435699667",
        "first_name": "Kolin",
        "last_name": "Hex",
        "avatar": "https://www.randomlists.com/img/people/john_bon_jovi.webp",
        "id": "10",
    },
]


class SetUpFiles(TestCase):
    def test_parser(self):
        parser = Parser(
            xml_file="accounts/sample_data/test_task.xml",
            csv_file=open("accounts/sample_data/test_task.csv"),
        )
        users_list = DataValidator(
            parser.parse_csv(), parser.parse_xml()
        ).validate_user_info()
        assert type(users_list) == list
        assert type(users_list[0]) == dict
        assert users_list == expected_data
