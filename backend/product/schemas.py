from backend import ma
from backend.product.models import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        ordered = True

user_schema = ProductSchema()
user_list_schema = ProductSchema(many=True) #list