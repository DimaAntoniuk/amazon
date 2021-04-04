import interfaces
from models import Product, Subgroup, Group, Customer, Payment, Cart, Seller
from app import db


class AccessProductManager(ProductManager):
    
    def get_by_id(self, id):
        return db.session.query(Product).get(id)
    
    def get_all(self):
        return db.session.query(Product).all()
    
    def remove(self, id):
        product = db.session.query(Product).get(id)
        db.session.delete(product)
    
    def add(self, name, subgroup_id=None, seller_id=None, cart_id=None):
        product = Product()
        product.name = name
        product.subgroup_id = subgroup_id
        product.seller_id = seller_id
        product.cart_id = cart_id
        db.session.add(product)


class AccessSubgroupManager(SubgroupManager):
    
    def get_by_id(self, id):
        return db.session.query(Subgroup).get(id)
    
    def get_all(self):
        return db.session.query(Subgroup).all()
    
    def remove(self, id):
        subgroup = db.session.query(Subgroup).get(id)
        db.session.delete(subgroup)
    
    def add(self, name, group_id=None):
        subgroup = Subgroup()
        subgroup.name = name
        subgroup.group_id = group_id
        db.session.add(subgroup)



class AccessGroupManager(GroupManager):
    
    def get_by_id(self, id):
        return db.session.query(Group).get(id)
    
    def get_all(self):
        return db.session.query(Group).all()
    
    def remove(self, id):
        group = db.session.query(Group).get(id)
        db.session.delete(group)
    
    def add(self, name):
        group = Group()
        group.name = name
        db.session.add(group)


class AccessCustomerManager(CustomerManager):
    
    def get_by_id(self, id):
        return db.session.query(Customer).get(id)
    
    def get_all(self):
        return db.session.query(Customer).all()
    
    def remove(self, id, ):
        customer = db.session.query(Customer).get(id)
        db.session.delete(customer)
    
    def add(self, name, address, phone_number, cart_id=None):
        customer = Customer()
        customer.name = name
        customer.address = address
        customer.phone_number = phone_number
        customer.cart_id = cart_id
        db.session.add(customer)


class AccessPaymentManager(PaymentManager):
    
    def get_by_id(self, id):
        return db.session.query(Payment).get(id)
    
    def get_all(self):
        return db.session.query(Payment).all()
    
    def remove(self, id):
        payment = db.session.query(Payment).get(id)
        db.session.delete(payment)
    
    def add(self, customer_id, card_type, card_number):
        payment = Payment()
        payment.customer_id = customer_id
        payment.card_type = card_type
        payment.card_number = card_number
        db.session.add(payment)


class AccessCartManager(CartManager):
    
    def get_by_id(self, id):
        return db.session.query(Cart).get(id)
    
    def get_all(self):
        return db.session.query(Cart).all()
    
    def remove(self, id):
        cart = db.session.query(Cart).get(id)
        db.session.delete(cart)
    
    def add(self, number_of_products, total):
        cart = Cart()
        cart.number_of_products = number_of_products
        cart.total = total
        db.session.add(cart)


class AccessSellerManager(SellerManager):
    
    def get_by_id(self, id):
        return db.session.query(Seller).get(id)
    
    def get_all(self):
        return db.session.query(Seller).all()
    
    def remove(self, id):
        seller = db.session.query(Seller).get(id)
        db.session.delete(seller)
    
    def add(self, name):
        seller = Seller()
        seller.name = name
        db.session.add(name)
