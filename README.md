# 🗃️ Django CRUD App with Authentication

This is a basic **CRUD (Create, Read, Update, Delete)** web application built with **Django** and **Bootstrap 5**, designed for managing customer records with authentication.

---

## 🚀 Features

- User login/logout functionality
- Add new customer records
- View record details
- Edit/update existing records
- Delete records
- Responsive Bootstrap-based UI
- Flash messages for user feedback

---

## 🧰 Tech Stack

- Python 3
- Django 4+
- Bootstrap 5.3 (CDN)
- SQLite (default Django database)

---

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Create a superuser (admin login)**:
   ```bash
   python manage.py createsuperuser

6. **Run the server**:
   ```bash
   python manage.py runserver

7. **Open your browser and go to**:
   ```bash
   http://127.0.0.1:8000/
