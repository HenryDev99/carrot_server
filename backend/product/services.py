from backend import db
from backend.product.models import Product

def get_list():
    res = db.session.query(Product).all()
    data_arry = []
    result = {}
    for data in res:
        temp_obj = {}
        temp_arry = []
        temp_obj['id'] = data.productIdx
        temp_obj['title'] = data.title
        temp_obj['content'] = data.content
        temp_obj['price'] = data.price
        temp_obj['userIdx'] = data.userIdx
        temp_obj['categoryIdx'] = data.categoryIdx
        temp_obj['status'] = data.status
        temp_obj['priceProposal'] = data.priceProposal

        if data.productPhotoUrl1 is not None:
            temp_arry.append(data.productPhotoUrl1)
        if data.productPhotoUrl2 is not None:
            temp_arry.append(data.productPhotoUrl2)
        if data.productPhotoUrl3 is not None:
            temp_arry.append(data.productPhotoUrl3)
        if data.productPhotoUrl4 is not None:
            temp_arry.append(data.productPhotoUrl4)
        if data.productPhotoUrl5 is not None:
            temp_arry.append(data.productPhotoUrl5)

        temp_obj['images'] = temp_arry
        data_arry.append(temp_obj)

    result['msg'] = 'ok'
    result['data'] = data_arry
    return result