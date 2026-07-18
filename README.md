# Employee Management System

A RESTful Employee Management API built using FastAPI and SQLModel.

## Features

- Create Employee
- Get All Employees
- Get Employee by ID
- Update Employee
- Delete Employee
- Search Employees by Department
- Get High Salary Employees

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Pydantic

## Installation

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /employees | Create Employee |
| GET | /employees | Get All Employees |
| GET | /employees/{id} | Get Employee by ID |
| PUT | /employees/{id} | Update Employee |
| DELETE | /employees/{id} | Delete Employee |
| GET | /department/{department} | Search by Department |
| GET | /high-salary | Employees with Salary > 50000 |

## Author

Purna Sai Kishore
