# Django Employee API (DRF)

This project is a simple Employee Management REST API built using Django and Django REST Framework.

It demonstrates how to work with serializers, models, and basic API structure for handling employee data.

---

## 🚀 Features

- Employee CRUD API (Create, Read, Update, Delete)
- Django REST Framework serializers
- JSON-based API responses
- Model-driven architecture
- Class-Based Views (CBV)
- Lightweight and extensible structure


---

## 📦 Tech Stack

<img src="https://skillicons.dev/icons?i=python,django" height="40"/> <br>
![DRF](https://img.shields.io/badge/Django%20REST-ff1709?style=for-the-badge&logo=django&logoColor=white)

- Django
- Django REST Framework
- Python
---

## 📊 Employee Fields

- emp_id
- first_name
- last_name
- email
- department
- designation
- salary
- joining_date
- City
- Address

---

## 🧠 Concepts I Learned
- Django Models  
- Django REST Framework Serializers  
- JSON Parsing & Rendering  
- Class-Based Views (CBV)  
- API Request Handling  
- HTTP Methods:
- GET (Retrieve data from API)
- GET → Retrieve employee data
- POST → Create new employee
- PUT → Update existing employee
- DELETE → Remove employee record
- Serializer Validation
- Request & Response Handling
- Working with JSON Data
---

## WIP 
## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees/` | Get all employees |
| GET | `/employees/id/` | Get single employee |
| POST | `/employees/` | Create employee |
| PUT | `/employees/id/` | Update employee |
| DELETE | `/employees/id/` | Delete employee |

---

## 👨‍💻 Author

**Sajjad Ali**

-[![Email](https://img.shields.io/badge/Email-000000?style=for-the-badge&logo=icloud&logoColor=white)](mailto:sajjadali.dev01@gmail.com) <br>
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sajjadali-fullstack/)

---


## 🔧 Setup Instructions

```bash
# Clone repository
git clone https://github.com/sajjadali-fullstack/rest-api-employee-system.git

# Download
pip install requests

# Go to project directory
cd withRest1

# Install dependencies
pip install django djangorestframework

# Run server
python manage.py runserver
