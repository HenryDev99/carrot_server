from datetime import datetime
from backend import db
from backend.product.models import Product

def get_list():
    res = db.session.query(Product).all()
    data_arry = []
    result = {}
    current_time = datetime.now()

    for data in res:
        temp_obj = {}
        temp_obj['id'] = data.productIdx
        temp_obj['title'] = data.title
        temp_obj['price'] = data.price
        temp_obj['userIdx'] = data.userIdx
        temp_obj['status'] = data.status
        temp_obj['time'] = str(current_time - data.createdAt)
        if data.productPhotoUrl1 is not None:
            temp_obj['images'] = data.productPhotoUrl1
        data_arry.append(temp_obj)

    result['msg'] = 'ok'
    result['data'] = data_arry
    return result