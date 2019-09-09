# Django library

## Overview
The main features that have currently been implemented are:
* There are models for User and book.
* Superuser can add new user at main page.
* Users can login, view a list of users and their books, add book, edit book.

## Quick Start
To get this project up and running locally on your computer:
```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python manage.py loaddata allDataFixture.json # in apps we have two another dump files for every app
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
```
* Open tab to `http://127.0.0.1:8000` to see the main site.