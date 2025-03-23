# 🚀 Task Management API

A robust Task Management API built with Django, providing authentication, task management, and notifications, with a fully Dockerized setup.

## 🌟 Features
- ✅ **CRUD for tasks**
- 🔐 **User authentication** via Django’s built-in session authentication
- 🔍 **Task status filtering**
- ⏳ **Rate-limited API**
- ☁️ **Simulated AWS Lambda notifications** (code implemented but not deployed)
- 🗄 **PostgreSQL database**
- 🐳 **Dockerized setup** for easy deployment
- 🔔 **Django signals** for task completion notifications
- 🧪 **Unit tests** for key functionalities

---

## 🛠 Setup Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/githubjmohit095/task-manager.git
cd task-manager/taskmanager
```

### 2️⃣ Configure PostgreSQL and `.env` File
Create a `.env` file in the root directory and add the following:
```ini
POSTGRES_DB=task_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DATABASE_URL=postgresql://postgres:password@db:5432/task_db
DEBUG=True
```

### 3️⃣ Run the Project Using Docker
```sh
docker-compose up --build -d
```
- `--build`: Builds the images.
- `-d`: Runs in detached mode.

### 4️⃣ Apply Migrations and Create a Superuser
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5️⃣ Access the Application
Open [http://localhost:8001/](http://localhost:8001/) in your browser.

---

## 📡 API Endpoints

### 🔑 User Authentication
| Method | Endpoint | Description |
|--------|----------|--------------|
| `POST` | `/api/users/register/` | Register a new user |
| `POST` | `/api/users/login/` | Log in user (Session-based authentication) |
| `POST` | `/api/users/logout/` | Log out user |
| `GET`  | `/api/users/` | List all users (Authenticated users only) |

### 📋 Task Management
| Method | Endpoint | Description |
|--------|----------|--------------|
| `GET`  | `/api/tasks/` | List all tasks |
| `POST` | `/api/tasks/` | Create a new task |
| `GET`  | `/api/tasks/{id}/` | Get task details |
| `PATCH` | `/api/tasks/{id}/` | Update a task |
| `DELETE` | `/api/tasks/{id}/` | Delete a task |

---

## 🧪 Running Unit Tests
Execute the following command to run unit tests:
```sh
docker-compose exec web python manage.py test
```
### ✅ Implemented Test Cases:
- User registration and authentication
- Task creation, retrieval, update, and deletion
- Rate-limited API endpoint validation
- Task filtering by status

---

## 🔔 Django Signals Implementation
- A **signal is triggered** when a task is marked as **completed**.
- This simulates an **AWS Lambda notification** (currently prints a log message).
- Future integration can use AWS Lambda for **real notifications**.

---

## 🚀 Future Improvements
- ✅ Deploy AWS Lambda notifications
- ✅ Implement API throttling for enhanced security
- ✅ Expand unit test coverage

---
---

### 👨‍💻 Author
**Mohit Joshi**  
📧 [Email](mailto:mannulegend8@gmail.com)  
🔗 [GitHub](https://github.com/githubjmohit095)

---
