# Inventory
Simple Django project that models products, categories, and tags for a construction supply store. Includes a search and filter page, Django admin interface, and sample data.

## Requirements

- Python 3.8+
- pip


## Setup & Run

### 1. Clone the project


### 2. Create and activate a virtual environment
```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Run migrations to set up the database
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

Visit **localhost:8000** to view the Inventory.
Click on Django Admin button to access the admin panel.

Admin login: `admin` / `admin123456`


## Assumptions & Notes

Assumptions:
A product can have many tags but just have 1 category.
Product does not have to have any category, however it will show up in the 'All categories'.
Product does not have to have any tags.

## AI Attribution

I used Claude to help me generate the base project structure and then I have modified it to fit the requirements of the task.

The product_list.html HTML/CSS styling and layout are AI generated but I have modified parts of the website to fit the requirement of the task,
including removing unnecessary content, and adding the filter button.

I have also use AI to assist with the filtering logic but I manually adjust the filtering logic to only include description.

I have used Claude to help generate 20 products that are related to construction, which I have added to the database through the admin interface.
