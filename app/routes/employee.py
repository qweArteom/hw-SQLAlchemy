from flask import render_template, Blueprint, request

from app.data.position import Position
from app.data.employee import Employee
from app.data.base import Session


employees_router = Blueprint("employees", __name__, url_prefix="/employees/")


@employees_router.get("/")
@employees_router.post("/")
def  add_employee():
    with Session() as session:
        if request.method == "POST":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            age = request.form.get("age")
            salary = request.form.get("salary")

            positions = request.form.getlist("positions")
            positions = session.query(Position).where(Position.id.in_(positions)).all()

            employee = Employee(first_name=first_name, last_name=last_name, age=age, salary=salary, positions=positions)
            session.add(employee)
            session.commit()

        employees = session.query(Employee).all()
        positions = session.query(Position).all()
        return render_template("employee/management.html", employees=employees, positions=positions, title="Додати нового працівника")


@employees_router.get("/<int:id>/")
def get_employee(id):
    with Session() as session:
        employee = session.query(Employee).where(Employee.id==id).first()
        return render_template("employee/info.html", title="Інформація про працівника", employee=employee)
