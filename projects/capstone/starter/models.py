from sqlalchemy import Column, String, Integer, Float, DateTime, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_path = 'postgres://rmzzyhjbgcmjkj:c0111010a63b2f67c07b84c3ef860d1b11c76440575127286f1e814dd55d2005@ec2-18-215-99-63.compute-1.amazonaws.com:5432/deofd1ev73pp7h'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #migrate = Migrate(app, db)
    
    #db.create_all()
    


'''
Client
Contains the client information
'''
class Client(db.Model): 
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable = False)
    surname = Column(String(120), nullable = False)
    id_number = Column(String(14), nullable = False, unique = True)
    email = Column(String(120), nullable = False)
    phone = Column(String(120), nullable = False)

    def __init__(self, first_name, surname, id_number, email, phone):
        self.first_name = first_name
        self.surname = surname
        self.id_number = id_number
        self.email = email
        self.phone = phone

    '''
    insert()
        inserts a new record into a database
        the record must have a unique identity number
        the record must have a unique id
        EXAMPLE
            client = Client(first_name=name, surname=surname, 
                            id_number = identiy number, email = email, 
                            phone = phone)
            client.insert()
    '''


    def insert(self):
        db.session.add(self)
        db.session.commit()

  
    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'surname': self.surname,
            'id_number': self.id_number,
            'email': self.email,
            'phone': self.phone
        }

'''
Product
Contains the product information
'''

class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable = False)
    description = Column(String(200), nullable = False)
    price = Column(Float(precision=2))

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


    def insert(self):
        db.session.add(self)
        db.session.commit()

  
    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'product': self.product_name,
            'description': self.description,
            'price': self.price
        }


''' 
Sales
Contains the client purchases of specific products
'''
class Sales(db.Model):
    __tablename__='sales'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    client_id = Column(Integer, db.ForeignKey('client.id'))
    product_id = Column(Integer,db.ForeignKey('product.id'))
    quantity = Column(Integer)
    product = db.relationship("Product", backref=db.backref('client'))
    client = db.relationship("Client", backref=db.backref('product'))

    def __init__(self, date, client_id, product_id, quantiy):
        self.date = date
        self.client_id = client_id
        self.product_id = product_id
        self.quantity = quantity

    def format(self):
        return {
            'id': self.id,
            'date': self.date,
            'client_id': self.client_id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }