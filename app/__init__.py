from flask import Flask

from app.routes.position import positions_route
from app.routes.employee import employees_router
from app.data.base import create_db
from app.data.position import Position
from app.data.employee import Employee


app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(positions_route)
app.register_blueprint(employees_router)

create_db()
