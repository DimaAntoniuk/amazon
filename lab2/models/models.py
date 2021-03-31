from app import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subgroup_id = db.Column(db.Integer, db.ForeignKey('subgroup.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=True)
    def __repr__(self):
        return f'Product: {self.name}'


class Subgroup(db.Model):
    __tablename__ = 'subgrpoup'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    products = db.relationship('Product', backref='subgroup', lazy=True)

    def __repr__(self):
        return f'Subgroup: {self.name}'


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subgroups = db.relationship('Subgroup', backref='group', lazy=True)

    def __repr__(self):
        return f'Group: {self.name}'


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))

    def __repr__(self):
        return f'Customer: [{self.name},
                {self.address}, {self.phone_number}]'


class Payment(db.Model):
    __tablename__ = 'payment'
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    card_type = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Payment: [{self.name},
                {self.card_type}, {self.card_number}]'

class Cart(db.Model):
    __tablename__ = 'cart'
    
    id = db.Column(db.Integer, primary_key=True)
    number_of_products = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    products = db.relationship('Product', backref='cart', lazy=True)
    customer = db.relationship('Customer', uselist=False, backref='cart', lazy=True)

    def __repr__(self):
        return f'Cart: [{self.number_of_products},
                {self.total}, {self.products}]'


class Seller(db.Model):
    __tablename__ = 'seller'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    products = db.relationship('Product', backref='seller', lazy=True)
    
    def __repr__(self):
        return f'Seller: {self.name}'