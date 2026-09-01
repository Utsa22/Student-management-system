# Student Management System

A beginner friendly Student Management System built with Django, HTML and CSS.

## Project Overview

This project is designed to demonstrate the basic concepts of Django web development through a simple Student Management System.

Users can register, log in, manage students and perform CRUD operations.

## Features

- User Registration
- User Login
- User Logout
- Authentication
- Authorization
- Django Admin Panel
- Add Student
- View Student List
- View Student Details
- Update Student
- Delete Student
- Search Students
- Class-Based Views
- Django Forms
- SQLite Database
- Django Messages
- User-based permissions
- Responsive HTML/CSS interface

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite
- Git
- GitHub

## CRUD Operations

The system supports all four basic CRUD operations:

- Create - Add a new student
- Read - View student information
- Update - Edit student information
- Delete - Remove a student

## Authentication

Users must log in to access the student management section.

Unauthenticated users are redirected to the login page.

## Authorization

A user can update or delete their own students.

Superusers can manage all students.

## Admin Panel

Django's built-in admin panel is used to manage students and users.

Admin URL:

`/admin/`

## Project Structure

```text
student_managements/
│
├── core/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── student_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .gitignore
├── manage.py
└── README.md
