from backend import db
from backend.product.models import Product

def get_list():
    res = db.session.query(Product).all()
    data_arry = []
    result = {}
    for data in res:
        temp = {}
        temp['title'] = data.title
        temp['content'] = data.content
        temp['price'] = data.price
        temp['userIdx'] = data.userIdx
        temp['categoryidx'] = data.categoryidx
        temp['status'] = data.status
        temp['priceProposal'] = data.priceProposal
        data_arry.append(temp)

    result['msg'] = 'ok'
    result['data'] = data_arry
    return result