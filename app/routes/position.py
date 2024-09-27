from flask import render_template, Blueprint, request

from app.data.base import Session
from app.data.position import Position


positions_route = Blueprint("positions", __name__, url_prefix="/positions/")



@positions_route.get("/")
@positions_route.post("/")
def add_position():
    with Session() as session:
        if request.method == "POST":
            name = request.form.get("name")
            position = Position(name=name)
            session.add(position)
            session.commit()

        positions = session.query(Position).all()

        return render_template("position/management.html", positions=positions, title="Список посад")


@positions_route.get("/<int:id>")
def get_position(id):
    with Session() as session:
        position = session.query(Position).where(Position.id == id).first()
        return render_template("position/info.html", position=position, title="Інформарція про посаду")
