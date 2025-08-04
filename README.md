# Employee Management System

A Django-based employee management system with REST API, JWT authentication, analytics dashboard, and Docker support.

<img width="1896" height="911" alt="image" src="https://github.com/user-attachments/assets/5cdca26a-8054-4536-ac8f-32ec86abf822" />

<img width="1901" height="906" alt="image" src="https://github.com/user-attachments/assets/7f4fc50b-e975-42fb-b716-14542ffd4871" />
<img width="1897" height="912" alt="image" src="https://github.com/user-attachments/assets/e211596c-a774-450d-819e-d93cc9d295f7" />
<img width="1901" height="915" alt="image" src="https://github.com/user-attachments/assets/eb0e92ab-7e63-4654-a179-a7ba8fdcdb4b" />



##  Features

-  **Employee Management**: Create, read, update, and delete employee records
-  **Department Organization**: Group employees by departments
-  **Attendance Tracking**: Record daily attendance (Present/Absent/Late)
-  **Performance Reviews**: Track employee performance ratings
-  **RESTful APIs**: Full CRUD via Django REST Framework
-  **JWT Authentication**: Secure endpoints using Simple JWT
-  **Analytics Dashboard**: Visualize attendance and department metrics with Chart.js
-  **Swagger API Docs**: Explore API interactively via Swagger UI (drf-yasg)
-  **Docker Support**: Fully containerized with Docker & docker-compose


## 🛠️ Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Backend       | Django 4.x, Django REST Framework |
| Database      | PostgreSQL               |
| Authentication| Simple JWT               |
| API Docs      | drf-yasg (Swagger)       |
| Charts        | Chart.js                 |

---

##  Setup Instructions

###  Prerequisites

- Python 3.10+
- PostgreSQL
- Docker (optional)

---

### 🔧 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/employee-management-system.git
   cd employee-management-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # For Linux/Mac
   venv\Scripts\activate           # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` file:

   ```ini
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=employee_db
   DB_USER=postgres
   DB_PASSWORD=yourpassword
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Seed sample data**
   ```bash
   python manage.py seed_data
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

---

###  Docker Setup

1. **Build and start containers**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   ```
   http://localhost:8000
   ```



  Authentication

- **Obtain JWT token**
   ```bash
   curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "yourpassword"}'
   ```

- **Use access token**
   ```bash
   curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/employees/
   ```



##  API Documentation

- **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)




## Analytics Dashboard

- Access at: [http://localhost:8000/charts/](http://localhost:8000/charts/)

### Charts:
- **Employees per Department** – Pie chart
- **Monthly Attendance** – Bar chart (Present, Absent, Late)



##  Required Environment Variables

```ini
SECRET_KEY=your-production-secret-key
DEBUG=False
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```


##  Project Structure

```
employee_project/
├── .env.example         # Environment config template
├── Dockerfile           # Docker setup
├── docker-compose.yml   # Docker orchestration
├── requirements.txt     # Python dependencies
├── manage.py            # Django CLI
├── employee_project/    # Project settings and URLs
├── employees/           # Employee CRUD logic
├── attendance/          # Attendance tracking
├── performance/         # Performance ratings
├── templates/           # HTML templates
```

