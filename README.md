# To-Do Backend with Django

This is a backend project created with Django. It provides basic CRUD functionality for a to-do list application.

## Features

- View a list of all to-do items
- Add a new to-do item
- Update an existing to-do item
- Delete a to-do item
- View details of a specific to-do item

## Requirements

- Python 3.x
- Django 3.x

## Usage

Once the server is running, you can access the following endpoints:

- `/`: View a list of all to-do items
- `/add/`: Add a new to-do item
- `/update/<int:pk>`: Update an existing to-do item (replace `<int:pk>` with the ID of the item to update)
- `/delete/<int:pk>`: Delete a to-do item (replace `<int:pk>` with the ID of the item to delete)
- `/detail/<int:pk>`: View details of a specific to-do item (replace `<int:pk>` with the ID of the item to view)

