# CityU Bank
This is a DBMS Project for course 5003 by team **HomeRun**.

## Overview

This web application creates a banking web-app for a fictitious bank named CityU bank.

###Features

* create a new user and get a unique account
* edit and store your personal information
* transfer money from your account to another
* apply for loans (to be confirmed by issuing branch)

![CityU Bank Model](https://raw.githubusercontent.com/hiiragimei/HomeRun/main/static/images/Banking%20DBMS.jpg)

## Prerequisites

1. A Terminal
2. Python 3.4 or above setup.
3. Django framework 2.0 or above installed.

## Quick Start

Assuming you have Python setup, run the following commands in root directory **HomeRun** \
(if you're on Windows you may use `python` or `python3` instead of `py -3` to start Python):

   ```
   pip3 install -r requirements.txt
   python3 manage.py runserver
   ```

1. Open a browser to `http://127.0.0.1:8000` to see the main site.
2. Open tab to `http://127.0.0.1:8000/admin/` to open the admin site.

*If cannot login to the admin site with password below, run the following commands*

   ```
   pip3 install -r requirements.txt
   py -3 manage.py createsuperuser
   python3 manage.py runserver
   ```

## Users Info

There are some users created for test.

###Superuser
Username: admin \
Password: admin

###Other users
Password: sdsc5003

## Disclaimer
This project was developed as a course assignment based on a fictitious bank. 
All users, account numbers and records are unreal.