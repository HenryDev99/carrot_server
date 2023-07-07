from datetime import timedelta

class Config:
    TESTING = False
    JWT_SECRET_KEY = "carrot"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://admin:aws4790!@database-1.cpyq6neohqa5.ap-northeast-2.rds.amazonaws.com/EOT?charset=utf8"
    JWT_SECRET_KEY = "carrot"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://admin:aws4790!@database-1.cpyq6neohqa5.ap-northeast-2.rds.amazonaws.com/EOT?charset=utf8"
class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://admin:aws4790!@database-1.cpyq6neohqa5.ap-northeast-2.rds.amazonaws.com/EOT?charset=utf8"
