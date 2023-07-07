from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, Resource, fields

from backend.api.user import protected
from backend.product.services import get_list

api = Namespace("product", description="Product API")

product_list_fields = api.model(
    "ProductList", {}
)

@api.doc(body=product_list_fields)
class GetList(Resource):
    @jwt_required(optional=True)
    def get(self):
        """product list"""
        if protected(get_jwt_identity()):
            return get_list()

api.add_resource(GetList, "/list")