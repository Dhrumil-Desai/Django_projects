# Django Projects Repository

## 📌 About

This repository contains all the Django projects that I developed during my **15-Day Summer Internship** at **Inlabz Technology**.

These projects were created to strengthen my understanding of Django, Python, database management, and web application development through hands-on practice.

## 🛠️ Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Django Admin

## 💻 Requirements

Before running the projects, make sure you have the following installed:

- Python 3.x
- PyCharm (or any Python IDE)
- Django

### Install Django

Open the terminal and run:

```bash
pip install django
```

### Download PyCharm

https://www.jetbrains.com/pycharm/download/

---

# 🚀 How to Set Up a Django Project

# ⚙️ Project Setup

> **Note:** All the commands below should be executed in the **PyCharm Terminal**.


## Step 1: Create a New Project

Open **PyCharm** and create a new Python project by selecting the desired project location.

## Step 2: Create a Virtual Environment

Create a virtual environment inside your project folder:

```bash
python -m venv .venv
```

## Step 3: Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

After activation, your terminal should look similar to:

```text
(.venv) C:\Users\YourName\Project>
```

---

## Step 4: Install Django

```bash
pip install django
```

Verify the installation:

```bash
python -m django --version
```

---

## Step 5: Create a Django Project

```bash
django-admin startproject project_name .
```

---

## Step 6: Create a Django App

```bash
python manage.py startapp app_name
```

## Step 7: Register the App

Open **settings.py** and add your app inside the `INSTALLED_APPS` list.

```python
INSTALLED_APPS = [
    ...
    'app_name',
]
```

## Step 8: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 9: Create a Superuser

```bash
python manage.py createsuperuser
```

Provide the following details:

- Username
- Email Address
- Password
- Confirm Password

## Step 10: Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

**Home Page**

```
http://127.0.0.1:8000/
```

**Django Admin Panel**

```
http://127.0.0.1:8000/admin/
```
---

## Step 11: Customize the Django Admin Panel (Optional)

If you want to change the default appearance of the Django Admin Panel, you can use third-party admin themes and styling packages.

Explore the available Django Admin themes here:

🔗 https://djangopackages.org/grids/g/admin-styling/

Popular packages include:

- Jazzmin
- Django Admin Interface
- Django Unfold
- Django Grappelli
- Django Suit
- Django SimpleUI

> **Note:** Always verify that the selected package is compatible with your installed Django version before installing it.

## Step 12: Create Your Models

Define your models inside:

```python
models.py
```

After making changes, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Step 13: Register Models in Django Admin

Register your models inside:

```python
admin.py
```

Restart the development server:

```bash
python manage.py runserver
```

# 📂 Repository Contents

This repository includes multiple Django projects developed during my internship, covering concepts such as:

- Django Models
- Django Admin Panel
- CRUD Operations
- Image Upload
- Foreign Keys
- Database Relationships
- Authentication
- SQLite Database
- Forms & Validation

---

# 📚 Learning Outcomes

During this internship, I gained practical experience in:

- Python Programming
- Django Framework
- Database Design
- Django ORM
- Admin Panel Customization
- Web Application Development
- Project Structure
- MVC (MVT) Architecture
- Git & GitHub

---

# 🤝 Feedback

If you have any suggestions or improvements, feel free to open an Issue or submit a Pull Request.

Your feedback is always appreciated!

---
