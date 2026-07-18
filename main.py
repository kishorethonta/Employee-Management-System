from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from contextlib import asynccontextmanager
from typing import Annotated

from models import Employee, EmployeeCreate


DATABASE_URL = "sqlite:///./employee.db"

engine = create_engine(DATABASE_URL, echo=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="Employee Management System",
              lifespan=lifespan)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

@app.post("/employees")
def create_employee(employee: EmployeeCreate,
                    session: SessionDep):

    new_employee = Employee.model_validate(employee)

    session.add(new_employee)
    session.commit()
    session.refresh(new_employee)

    return {
        "message": "Employee created successfully",
        "data": new_employee
    }

@app.get("/employees", response_model=list[Employee])
def get_employees(session: SessionDep):

    employees = session.exec(
        select(Employee)
    ).all()

    return employees

@app.get("/employees/{employee_id}",
         response_model=Employee)
def get_employee(employee_id: int,
                 session: SessionDep):

    employee = session.get(
        Employee,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@app.put("/employees/{employee_id}",
         response_model=Employee)
def update_employee(
        employee_id: int,
        update: EmployeeCreate,
        session: SessionDep):

    employee = session.get(
        Employee,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee.name = update.name
    employee.department = update.department
    employee.salary = update.salary
    employee.email = update.email

    session.add(employee)
    session.commit()
    session.refresh(employee)

    return employee

@app.delete("/employees/{employee_id}")
def delete_employee(
        employee_id: int,
        session: SessionDep):

    employee = session.get(
        Employee,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    session.delete(employee)
    session.commit()

    return {
        "message": "Employee deleted successfully"
    }

@app.get("/department/{department}")
def get_department_employees(
        department: str,
        session: SessionDep):

    employees = session.exec(
        select(Employee).where(
            Employee.department == department
        )
    ).all()

    return employees

@app.get("/high-salary")
def high_salary_employees(
        session: SessionDep):

    employees = session.exec(
        select(Employee).where(
            Employee.salary > 50000
        )
    ).all()

    return employees