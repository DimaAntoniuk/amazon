from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/amazon.db'
db = SQLAlchemy(app)

from models import Product, Subgroup, Group, Customer, Payment, Cart, Seller

db.create_all()
db.session.commit()