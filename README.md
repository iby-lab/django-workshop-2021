# Django Workshop 2021
Example Django project for IBY Hacks+ 2021 Django workshop.

This project requires Python 3.

# Table of Contents

* [Setup](#Setup)
* [Essential Commands Cheat Sheet](#Essential-Commands-Cheat-Sheet)

# Setup

Start a virtual environment (Windows 10)
```bash
python -m venv .venv
```

Open virtual environment
```bash
.venv/Scripts/Activate.ps1
```

[Use this repo](##Use-this-repository)
[Start your own project](##Start-your-own-project)

## Use this repository

Install required packages
```bash
pip install -r requirements.txt
```

Enter the project directory
```bash
cd mysite
```

Run the Django project
```bash
python manage.py runserver
```

The site should be locally available at 127.0.0.1:8000

## Start your own project

Install Django
```bash
pip install django
```

To create your own project, use the command:
```bash
django-admin startproject your_project_name
```

# Essential Commands Cheat Sheet

## Creating Django applications

Start a project:
```bash
django-admin startproject your_project_name
```

Run the project:
```bash
cd project_name
python manage.py runserver
```

Start a new app:
```bash
python manage.py startapp
```

## Database things

Push changes to models
```bash
python manage.py makemigrations
```

Make changes to database
```bash
python manage.py migrate
```

Create a superuser/admin
```bash
python manage.py createsuperuser
```


