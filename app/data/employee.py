from typing import List

from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data.position import Position
from app.data.base import Base
from app.data.associates import position_employee_assoc


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()
    salary: Mapped[float] = mapped_column(Float())
    positions: Mapped[List[Position]] = relationship(secondary=position_employee_assoc)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
