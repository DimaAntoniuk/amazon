from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


def extract(obj, columns, values, separator = ','):
    columns_list = columns.split(separator)
    values_list = values.split(separator)
    assert len(columns_list) == len(values_list)
    for column, value in zip(columns_list, values_list):
        if hasattr(obj, column) and column != 'id':
            setattr(obj, column, value)


class Cart(Base):
    __tablename__ = 'cart'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_products = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    products = relationship('Product', backref='cart', lazy=True)
    customer = relationship('Customer', uselist=False, backref='cart', lazy=True)

    def from_csv(self, columns, values, separator=','):
       extract(self, columns, values, separator)

    def __repr__(self):
        string =  f'Cart: ' 
        if hasattr(self, 'id'):
            string += f'{self.id}'
        string += f'number_of_products:{self.number_of_products}, total:{self.total}'
        return string


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    subgroups = relationship('Subgroup', backref='group', lazy=True)

    def from_csv(self, columns, values, separator=','):
       extract(self, columns, values, separator)

    def __repr__(self):
        string = f'Group: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}'
        return string


class Subgroup(Base):
    __tablename__ = 'subgroup'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey('group.id'))
    products = relationship('Product', backref='subgroup', lazy=True)

    def from_csv(self, columns, values, separator=','):
       extract(self, columns, values, separator)

    def __repr__(self):
        string = f'Subgroup: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}'
        return string


class Seller(Base):
    __tablename__ = 'seller'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(99), nullable=False)
    products = relationship('Product', backref='seller', lazy=True)
    
    def from_csv(self, columns, values, separator=','):
       extract(self, columns, values, separator)

    def __repr__(self):
        string = f'Seller: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}'
        return string


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    subgroup_id = Column(Integer, ForeignKey('subgroup.id'))
    seller_id = Column(Integer, ForeignKey('seller.id'))
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=True)
    
    def from_csv(self, columns, values, separator=','):
       extract(self, columns, values, separator)

    def __repr__(self):
        string = f'Product: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}, subgroup_id:{self.subgroup_id}, seller_id:{self.seller_id}, cart_id:{self.cart_id}'
        return string


class Payment(Base):
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    card_type = Column(String(50), nullable=False)
    card_number = Column(Integer, nullable=False)

    def from_csv(self, columns, values, separator=','):
       extract(self, columns, values, separator)

    def __repr__(self):
        string = f'Payment: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'customer_id:{self.customer_id}, card_type:{self.card_type}, card_number:{self.card_number}'
        return string


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    phone_number = Column(Integer, nullable=False)
    cart_id = Column(Integer, ForeignKey('cart.id'))

    def from_csv(self, columns, values, separator=','):
       extract(self, columns, values, separator)

    def __repr__(self):
        string = f'Customer: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'name:{self.name}, address:{self.address}, phone_number:{self.phone_number}'
        return string
