# CityU Bank

This is a DBMS Project for course SDSC5003 by team **HomeRun**.

## Overview

This web application creates a web-app for a fictitious bank named **CityU bank**.

## Features

* create a new user and get a unique account
* edit and store your personal information
* transfer money from your account to another
* apply for loans (to be confirmed by issuing branch)

## ER Diagram

![CityU Bank Model](https://raw.githubusercontent.com/hiiragimei/HomeRun/main/static/images/Banking%20DBMS.jpg)

## Requrement

    Python 3.4
    Django framework 2.0

## Quick Start

Run the following commands in root directory `/HomeRun`.

```
pip3 install -r requirements.txt
pyhon3 manage.py runserver
```

1. Open a browser to `http://127.0.0.1:8000` to see the main site.
2. Open tab to `http://127.0.0.1:8000/admin/` to open the admin site.

*or run the following commands*

```sh
pip3 install -r requirements.txt
python3 manage.py createsuperuser
python3 manage.py runserver
```

## Users Info

There are some users created for test.

### Superuser
Username: admin \
Password: admin

### Other users
Password: sdsc5003

## Disclaimer
This project was developed as a course assignment based on a fictitious bank. 
All users, account numbers and records are unreal.
