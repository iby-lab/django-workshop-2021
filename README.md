# Django Workshop 2021
Example Django project for IBY Hacks+ 2021 Django workshop.

This project requires Python 3.

# Table of Contents

* [Setup](#Setup)
  * [Use this repo](#Use-this-repository)
  * [Start your own project](#Start-your-own-project)
* [Templates](#Templates)
  * [Loading base templates](#Loading-base-templates)
  * [Loading static files](#Loading-static-files)
  * [Links](#Links)
  * [For loops](#For-loops)
  * [If statements](#If-statements)
* [Models](#Models)
* [Essential Commands Cheat Sheet](#Essential-Commands-Cheat-Sheet)
  * [Creating a django application](#Creating-django-applications)
  * [Database things](#Database-things)

# Setup

Start a virtual environment (Windows 10)
```bash
python -m venv .venv
```

Open virtual environment
```bash
.venv/Scripts/Activate.ps1
```

[Use this repo](#Use-this-repository)\
[Start your own project](#Start-your-own-project)

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

# Templates

Templates are the way Django reduces redundancy in front-end code. Once a template is made, it can be used anywhere in the project.

## Loading base templates

When creating a base template, specify "blocks" for further content
```html
{% block block_name %}
{% endblock %}
```

To access this template, use extend the file, then use the block name
```html
{% extends 'base.html' %}

{% block block_name %}
    <div class="your-content">
    </div>
{% endblock %}
```

## Loading static files

To load static files, load them and then refer to them in the tag href
```html
{% load static %}

<head>
    <link rel="stylesheet" href="{% static 'static_file.css' %}">
</head>
```

## Links

Use the url keyword to create variable urls in an a tag
```html
<a href="{% url 'view_name' %}">
```

## For loops

Use the Django for loop format
```html
{% for var in vars %}
{% endfor %}
```

## If statements

Use the Django if statement format
```html
{% if condition %}
    <div class="show-this"></div>
{% elif %} <!--If applicable-->
    <div class="show-this"></div>
{% else %}
    <div class="show-this"></div>
```

# Models

A model is a data field saved in the project database.

Models are generally similar to the below format, found in the models.py module of the proper app:
```python
from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    text = models.TextField()
```

Don't forget to create an admin in admin.py to see your model in the Django admin page.
```python
from django.contrib import admin
from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    fields = ["title", "author", "date_created", "text"]

admin.site.register(BlogPost, BlogPostAdmin)
```

Further reading: \
[Django documentation for creating a custom user model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/)\
[View Django documentation for all available field types](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

# Essential Commands Cheat Sheet

## Creating Django applications

Start a project
```bash
django-admin startproject your_project_name
```

Run the project
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


