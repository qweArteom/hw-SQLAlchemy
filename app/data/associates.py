from sqlalchemy import Table, Column, ForeignKey

from app.data.base import Base


position_employee_assoc = Table(
    "position_employee_assoc",
    Base.metadata,
    Column(
        "position_id",
        ForeignKey("positions.id"),
        primary_key=True,
    ),
    Column(
        "employee_id",
        ForeignKey("employees.id"),
        primary_key=True,
    ),
)
