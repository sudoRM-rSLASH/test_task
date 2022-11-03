# Instruction:

### Setup:

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser` # and create administrator

### Start

`python manage.py runserver`

### Notes

For create new users or see all created users login as administrator on:
http://127.0.0.1:8000/signin/

You can login as created user by username and password.

For launch tests use:

`python manage.py test`
