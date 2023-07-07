from backend import ma
from backend.product.models import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        ordered = True

product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True) #list