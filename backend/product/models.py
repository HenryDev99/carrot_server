from backend import db

Column = db.Column
Model = db.Model

#product table
class Product(Model):
    __tablename__ = "product"

    productIdx = Column(db.Integer, primary_key=True)
    title = Column(db.String(255), nullable=False)
    content = Column(db.String(255), nullable=False)
    price = Column(db.Integer, nullable=False)
    userIdx = Column(db.String(100), nullable=False)
    categoryIdx = Column(db.Integer, nullable=False)
    createdAt = Column(db.DateTime, nullable=False)
    updatedAt = Column(db.DateTime, nullable=True)
    status = Column(db.String(10), nullable=False)
    regionIdx = Column(db.Integer, nullable=True)
    priceProposal = Column(db.String(45), nullable=True)
    productPhotoUrl1 = Column(db.String(250), nullable=True)
    productPhotoUrl2 = Column(db.String(250), nullable=True)
    productPhotoUrl3 = Column(db.String(250), nullable=True)
    productPhotoUrl4 = Column(db.String(250), nullable=True)
    productPhotoUrl5 = Column(db.String(250), nullable=True)

    def __init__(self, productIdx, title, content, price, userIdx, categoryIdx, createdAt, updatedAt, status, regionIdx, priceProposal, productPhotoUrl1, productPhotoUrl2, productPhotoUrl3, productPhotoUrl4, productPhotoUrl5):
        self.productIdx = productIdx
        self.title = title
        self.content = content
        self.price = price
        self.userIdx = userIdx
        self.categoryIdx = categoryIdx
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.status = status
        self.regionIdx = regionIdx
        self.priceProposal = priceProposal
        self.productPhotoUrl1 = productPhotoUrl1
        self.productPhotoUrl2 = productPhotoUrl2
        self.productPhotoUrl3 = productPhotoUrl3
        self.productPhotoUrl4 = productPhotoUrl4
        self.productPhotoUrl5 = productPhotoUrl5

    def __repr__(self):
        return f"<Product {self.title} - {self.content}>"