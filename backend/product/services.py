from datetime import datetime
from sqlalchemy import and_
from backend import db
from backend.product.models import Product
from backend.user.models import User


def get_list():
    products = db.session.query(Product).all()
    data_arry = []
    result = {}
    current_time = datetime.now()

    for data in products:
        temp_obj = {}
        user = db.session.query(User).filter(User.id == data.userIdx).first()
        temp_obj['id'] = data.productIdx
        temp_obj['title'] = data.title
        temp_obj['price'] = data.price
        temp_obj['userIdx'] = data.userIdx
        temp_obj['status'] = data.status
        temp_obj['time'] = str(current_time - data.createdAt)
        temp_obj['region'] = user.region
        if data.productPhotoUrl1 is not None:
            temp_obj['images'] = data.productPhotoUrl1
        data_arry.append(temp_obj)

    result['msg'] = 'ok'
    result['data'] = data_arry
    return result