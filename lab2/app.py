from setup import app, db
from models.models import Product, Subgroup, Group, Customer, Payment, Cart, Seller

with app.app_context():
    # db.drop_all(app=app)
    db.create_all(app=app)
    print('1') if db.session.query(Product).all() else print('0')
    