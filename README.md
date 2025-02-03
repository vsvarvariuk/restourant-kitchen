# restaurant-kitchen

## Test user
Use next user:
- login: admin
- password: admin12345

1. Follow the link:
    ```bash
    https://restourant-kitchen.onrender.com

## Project Description
This project is a management system for a restaurant that helps improve communication and organization among chefs.  
It allows you to:
- Create new dishes and dish types.
- Assign chefs responsible for preparing each dish.
- Add ingredients to dishes through a user-friendly interface.

## Key Features
- Manage a list of dish types (e.g., appetizers, main courses, desserts).
- Create and edit dishes with assigned responsible chefs.
- Manage ingredients with a Many-to-Many relationship to dishes.
- Intuitive admin interface for content management.

## Database Structure
The project includes the following models:
1. **Chef** — stores information about chefs.
2. **DishType** — stores types of dishes.
3. **Dish** — stores dishes linked to dish types and chefs.
4. **Ingredient** — stores ingredients, linked to dishes via a Many-to-Many relationship.

## Requirements
- Python 3.13
- Django 4.2 or later
- SQLite (default) or another database system

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate #For Linux/macOS
   

   python -m venv venv
   venv\Scripts\activate #For windows
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply database migrations:
   ```bash
   python manage.py migrate

5. Run the development server:
   ```bash
   python manage.py runserver
6. Open http://127.0.0.1:8000 in your browser to view the site or http://127.0.0.1:8000/admin to access the admin panel.