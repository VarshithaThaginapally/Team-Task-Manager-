# 🧑‍💻 Team Task Manager

## 📌 Project Description
Team Task Manager is a full-stack web application developed to help teams manage tasks efficiently.  
The application allows users to register, log in, create tasks, track progress, and manage task completion through a dashboard.

This project demonstrates:
- Full-stack web development
- Database integration
- Authentication system
- CRUD operations
- Deployment using Railway

---

# 🚀 Features

## 🔐 Authentication
- User Signup
- User Login
- Session Management
- Logout Functionality

## 📋 Task Management
- Add New Tasks
- View Tasks
- Mark Tasks as Completed
- Delete Tasks

## 📊 Dashboard
- Display all tasks
- Task status tracking
- Pending & Completed task monitoring

## 🛡️ Security & Validation
- Session-based authentication
- Protected dashboard routes
- Form handling and validations

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Programming |
| Flask | Web Framework |
| MySQL | Database |
| HTML | Frontend Structure |
| CSS | Styling |
| Git & GitHub | Version Control |
| Railway | Deployment Platform |
| Gunicorn | Production Server |

---

# 📂 Project Structure

```text
TEAM-TASK-MANAGER/
│
├── app.py
├── Procfile
├── requirements.txt
├── runtime.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/VarshithaThaginapally/Team-Task-Manager-.git
```

---

## 2️⃣ Open Project Folder

```bash
cd TEAM-TASK-MANAGER
```

---

## 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

## Create Database

```sql
CREATE DATABASE taskmanager;
```

---

## Create Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(20)
);
```

---

## Create Tasks Table

```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    status VARCHAR(50),
    user_id INT
);
```

---

# ▶️ Running the Application

```bash
python app.py
```

Application runs on:
```text
http://127.0.0.1:5000
```

---

# 🌐 Deployment

The application is deployed using Railway.

## Live Deployment URL
https://team-task-manager-production-95aa.up.railway.app

---

# 🔗 GitHub Repository

https://github.com/VarshithaThaginapally/Team-Task-Manager-

---

# 🎥 Demo Video

The demo video includes:
- Project overview
- Authentication system
- Task management
- Dashboard functionality
- Deployment explanation

---

# 📚 Learning Outcomes

Through this project, the following concepts were implemented:
- Flask Web Development
- MySQL Integration
- CRUD Operations
- Authentication & Sessions
- Deployment with Railway
- GitHub Version Control

---

# 👩‍💻 Author

### Varshitha Thaginapally

