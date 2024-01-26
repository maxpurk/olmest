# MyERM Project

## Overview

MyERM (My Equipment Rental Marketplace) is a Python-based web application designed as a platform for renting and selling medical equipment. This project was undertaken as my first hands-on experience with Python and web development, serving as a learning journey through the intricacies of web application development using the Django framework.

## Features

User Profiles: Allows users to create and manage their profiles.
Product Listings: Enables sellers to list their medical equipment for rent or sale.
Buyers Interface: Facilitates buyers in browsing available equipment and initiating purchase or rental.
Admin Panel: A comprehensive admin interface to manage users, products, and other site data.
Dynamic Web Pages: Includes various web pages like home, confirm upload, create listing, and a buy or sell interface.

## Directory Structure

products/: Contains the models, views, forms, and admin configuration for product-related features.
profiles/: Manages user profile models and views.
buyers/, sellers/, and pages/: Handle the respective functionalities for different user roles and site pages.
static/: Stores static files like images.
templates/: Contains HTML templates for the web pages.
migrations/: Manages database migrations for each app.

## Tools and Technologies

Python: Primary programming language.
Django: Web framework for building the application.
SQLite3: Database used for storing application data.
HTML/CSS: For structuring and styling web pages.

## Installation and Setup


Clone the Repository:

```bash
git clone [repository-url]
```
Install Dependencies:
Navigate to the project directory and install dependencies using:

```bash
pip install -r requirements.txt
```

Initialize the Database:
Set up the database by running migrations:

```bash
python manage.py migrate
```

Run the Server:
Start the Django development server:

```bash
python manage.py runserver
```

## Learning Outcomes

Gained fundamental knowledge of Python and Django.
Learned about MVC architecture and how Django implements it.
Understood the workflow of web applications from front-end to back-end.
Developed skills in database management and web development best practices.

## Future Scope

Implementing advanced features like payment integration.
Enhancing the user interface for better user experience.
Adding API endpoints to make the platform more flexible and interactive.
This project was an enriching experience that laid the foundation for my future endeavors in Python and web development. The challenges encountered and the knowledge gained have been invaluable in understanding the full spectrum of building a web application.

## Current State
Discontinued 