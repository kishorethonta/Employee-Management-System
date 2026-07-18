from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    department: str
    salary: float
    email: EmailStr


class EmployeeCreate(SQLModel):
    name: str
    department: str
    salary: float
    email: EmailStr