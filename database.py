from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Image(db.Model):
    __tablename__ = 'Image'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    path = db.Column(db.String(40), nullable=False)


class Product(db.Model):
    __tablename__ = 'productlist'

    Phone = db.Column(db.String(40), nullable=False, primary_key=True)
    Version = db.Column(db.String(40), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Sales = db.Column(db.Integer, nullable=False)

    def __init__(self, phone, version, price, sales):
        self.Phone = phone
        self.Version = version
        self.Price = price
        self.Sales = sales


class User(db.Model):
    __tablename__ = 'UserMixin'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    path = db.Column(db.String(40), nullable=False)