# flask-todo-app-demo
flask-todo-app-demo
#  Flask To-Do App Demo

A simple **Task Manager (To-Do List)** web application built with **Flask** and **SQLite**.  
Users can **add, delete, and mark tasks as completed**.  
The UI is styled with **Bootstrap**, and the app is ready for deployment on **Render** or **Heroku**.

---

##  Problem Statement
Build a simple task management web application using Flask, allowing users to add, delete, and mark tasks as completed.

---

##  Week-Wise Plan

### **Week 1**
- Learn Flask fundamentals: routing, templates, rendering.
- Create an HTML form to add tasks.  
 **Deliverable:** Basic Flask app running locally, able to accept task input.

### **Week 2**
- Implement Add/Delete/Complete task functionalities.
- Store tasks temporarily in memory (Python list).  
 **Mid-Project Review:**  
- Core To-Do functionality in place.  
- UI updates task list in real-time.  

### **Week 3**
- Connect app to **SQLite** for persistent storage.
- Enhance UI with **Bootstrap styling**.  
 **Deliverable:** Tasks persist even after restart, with improved UI.

### **Week 4**
- Finalize features and perform testing.
- (Optional) Deploy on **Render** or **Heroku**.
- Write documentation & usage guide.  
 **Final Project Review:**  
- Fully functional Flask To-Do app.  
- Deployment link (optional).  
- Complete documentation with screenshots.  

---

##  Project Structure
flask-todo-app-demo/
│
├── app.py # Main Flask application (with SQLite + SQLAlchemy)
├── requirements.txt # Dependencies
├── Procfile # Deployment config (Heroku/Render)
├── runtime.txt # (optional) Python version
│
├── templates/ # HTML templates
│ ├── base.html # Bootstrap layout
│ └── index.html # To-Do list page
│
├── static/ # CSS, JS, images (optional)
│
└── todo.db # SQLite database (auto-created locally)

##  Installation (Local Setup)

Clone repo:
```bash
git clone https://github.com/alurichowdary/flask-todo-app-demo.git
cd flask-todo-app-demo

Create virtual environment (Windows):

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

flask run


 App runs at: http://localhost:5000

 Requirements:

Dependencies from requirements.txt:

Flask==3.0.3
Flask-SQLAlchemy==3.1.1
gunicorn==23.0.0
SQLAlchemy==2.0.32


Optional (for testing / Postgres):

pytest==8.3.2
psycopg2-binary==2.9.9

 Deployment:
Render Deployment

Push repo to GitHub.

Log into Render
 → New → Web Service → Connect Repo.

Build Command:

pip install -r requirements.txt


Start Command:

gunicorn app:app


Environment Variables:

For SQLite (dev):

DATABASE_URL=sqlite:///todo.db


For PostgreSQL (prod):

DATABASE_URL=postgresql://<user>:<password>@<host>/<db>

 Usage:

Open app in browser.

Add tasks using input box.

 Click Complete to mark tasks done.

 Click Delete to remove tasks.

 Final Deliverables

Fully functional Flask To-Do app

Persistent storage with SQLite

Bootstrap-styled UI

Deployment-ready on Render/Heroku