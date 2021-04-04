from setup import db


class Cart(db.Model):
    __tablename__ = 'cart'
    
    id = db.Column(db.Integer, primary_key=True)
    number_of_products = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    products = db.relationship('Product', backref='cart', lazy=True)
    customer = db.relationship('Customer', uselist=False, backref='cart', lazy=True)

    def __repr__(self):
        string =  f'Cart: ' 
        if hasattr(self, 'id'):
            string += f'{self.id}'
        string += f'number_of_products:{self.number_of_products}, total:{self.total}'
        return string


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subgroups = db.relationship('Subgroup', backref='group', lazy=True)

    def __repr__(self):
        string = f'Group: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}'
        return string


class Subgroup(db.Model):
    __tablename__ = 'subgroup'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    products = db.relationship('Product', backref='subgroup', lazy=True)

    def __repr__(self):
        string = f'Subgroup: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}'
        return string


class Seller(db.Model):
    __tablename__ = 'seller'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    products = db.relationship('Product', backref='seller', lazy=True)
    
    def __repr__(self):
        string = f'Seller: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}'
        return string


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subgroup_id = db.Column(db.Integer, db.ForeignKey('subgroup.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    
    def __repr__(self):
        string = f'Product: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}, subgroup_id:{self.subgroup_id}, seller_id:{seller_id}, cart_id:{cart_id}'
        return string


class Payment(db.Model):
    __tablename__ = 'payment'
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    card_type = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        string = f'Payment: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}, card_type:{self.card_type}, card_number:{self.card_number}'


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))

    def __repr__(self):
        return f'Customer: [{self.name},\
                {self.address}, {self.phone_number}]'
