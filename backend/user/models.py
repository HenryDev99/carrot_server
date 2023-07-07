from backend import db

Column = db.Column
Model = db.Model

#user table
class User(Model):
    __tablename__ = "user"

    phoneNumber = Column(db.String(45), primary_key=True)
    id = Column(db.String(50), nullable=False)
    email = Column(db.String(50), nullable=False)
    name = Column(db.String(20), nullable=False)
    password = Column(db.String(20), nullable=False)
    createAt = Column(db.DateTime, nullable=True)
    updateAt = Column(db.DateTime, nullable=True)
    status = Column(db.String(45), nullable=False)
    usrNickname = Column(db.String(45), nullable=True)
    imgUrl = Column(db.String(200), nullable=True)
    mannerTamp = Column(db.Numeric(precision=4, scale=1), nullable=False, default=36.5)
    tradeRate = Column(db.Numeric(precision=4, scale=1), nullable=False, default=0)
    responseRate = Column(db.Numeric(precision=4, scale=1), nullable=False, default=0)
    region = Column(db.String(200), nullable=True)

    def __init__(self, phoneNumber, id, email, name, password, createAt, status, usrNickname, imgUrl, mannerTamp, tradeRate, responseRate, region):
        self.phoneNumber = phoneNumber
        self.id = id
        self.email = email
        self.name = name
        self.password = password
        self.createAt = createAt
        self.status = status
        self.usrNickname = usrNickname
        self.imgUrl = imgUrl
        self.mannerTamp = mannerTamp
        self.tradeRate = tradeRate
        self.responseRate = responseRate
        self.region = region

    def __repr__(self):
        return f"<User {self.id} - {self.email}>"