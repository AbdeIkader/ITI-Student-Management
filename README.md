# 🎓 ITI Student Management Project

This is a small Django project I built for ITI training to practice working with **Django models, forms, templates**, and CRUD operations (Create, Read, Update, Delete).

The project allows you to manage students and their courses easily.

---

## 🧠 What the project does

- Add, edit, delete students  
- Upload student profile pictures  
- Connect students with courses (ManyToMany relationship)  
- Validate student age (must be 18+)  
- View all students and see their details  
- Simple, clean Bootstrap-based UI  

---

## ⚙️ How to run it

Follow these steps to set up and run the project on your machine 👇

### 1️⃣ Clone the repository
```bash
git clone https://github.com/AbdeIkader/ITI-Student-Management.git
cd iti-student-management

### 2️⃣ Create a virtual environment

```bash
python -m venv env
```

Activate it:

* **Windows:** `env\Scripts\activate`
* **macOS/Linux:** `source env/bin/activate`

---

### 3️⃣ Install the required packages

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the migrations

This will create the database and tables.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create a superuser (optional)

To log into Django admin and manage data manually:

```bash
python manage.py createsuperuser
```

Then access it from:

```
http://127.0.0.1:8000/admin/
```

---

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

Now open your browser and go to:

```
http://127.0.0.1:8000/
```

---

## 🗂️ Project structure (main idea)

```
iti_proj/
├── course/               # Course app (course model)
├── student/              # Student app (student model + forms + views)
├── media/students/       # Uploaded student images
├── db.sqlite3            # Local database (ignored in git)
└── manage.py
```

---

## 🧾 Notes

* All uploaded photos are stored in the `media/students/` folder.
* Age validation: Student must be **18 years or older**.
* Database used: SQLite (you can switch to PostgreSQL easily).
* The app uses Django’s built-in form system.

---

## 💻 Technologies Used

* Python 3.14
* Django 5.x
* SQLite
* Bootstrap for styling

---

## 🧑‍💻 Author

Created by **Abdelkader** as part of ITI training.
This project was mainly for learning purposes — focusing on Django’s forms, models, and CRUD flow.

---
