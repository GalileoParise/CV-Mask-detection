from flask import Blueprint

main_bp = Blueprint("main", __name__)

import app.main.routes
