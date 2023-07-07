from flask import Blueprint
from flask_restx import Api

from backend.api.user import api as user_ns
from backend.api.product import api as product_ns

api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="EveryOneTrip REST API", description="A REST API build with Flask")

api.add_namespace(user_ns)
api.add_namespace(product_ns)