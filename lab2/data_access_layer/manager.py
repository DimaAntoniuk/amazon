from interfaces import ProductManager, SubgroupManager, GroupManager,\
                       CustomerManager, PaymentManager, CartManager, SellerManager
from models.models import Product, Subgroup, Group, Customer, Payment, Cart, Seller


class AccessProductManager(ProductManager):
    def __init__(self, session):
        self.session = session
    
    def get_by_id(self, id):
        return self.session.query(Product).get(id)
    
    def get_all(self):
        return self.session.query(Product).all()
    
    def remove(self, id):
        product = self.session.query(Product).get(id)
        self.session.delete(product)
    
    def add(self, name, subgroup_id=None, seller_id=None, cart_id=None):
        product = Product()
        product.name = name
        product.subgroup_id = subgroup_id
        product.seller_id = seller_id
        product.cart_id = cart_id
        self.session.add(product)
    
    def add_from_csv(self, columns, values):
        product = Product()
        product.from_csv(columns, values)
        self.session.add(product)


class AccessSubgroupManager(SubgroupManager):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id):
        return self.session.query(Subgroup).get(id)
    
    def get_all(self):
        return self.session.query(Subgroup).all()
    
    def remove(self, id):
        subgroup = self.session.query(Subgroup).get(id)
        self.session.delete(subgroup)
    
    def add(self, name, group_id=None):
        subgroup = Subgroup()
        subgroup.name = name
        subgroup.group_id = group_id
        self.session.add(subgroup)

    def add_from_csv(self, columns, values):
        subgroup = Subgroup()
        subgroup.from_csv(columns, values)
        self.session.add(subgroup)



class AccessGroupManager(GroupManager):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id):
        return self.session.query(Group).get(id)
    
    def get_all(self):
        return self.session.query(Group).all()
    
    def remove(self, id):
        group = self.session.query(Group).get(id)
        self.session.delete(group)
    
    def add(self, name):
        group = Group()
        group.name = name
        self.session.add(group)

    def add_from_csv(self, columns, values):
        group = Group()
        group.from_csv(columns, values)
        self.session.add(group)


class AccessCustomerManager(CustomerManager):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id):
        return self.session.query(Customer).get(id)
    
    def get_all(self):
        return self.session.query(Customer).all()
    
    def remove(self, id, ):
        customer = self.session.query(Customer).get(id)
        self.session.delete(customer)
    
    def add(self, name, address, phone_number, cart_id=None):
        customer = Customer()
        customer.name = name
        customer.address = address
        customer.phone_number = phone_number
        customer.cart_id = cart_id
        self.session.add(customer)
    
    def add_from_csv(self, columns, values):
        customer = Customer()
        customer.from_csv(columns, values)
        self.session.add(customer)


class AccessPaymentManager(PaymentManager):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id):
        return self.session.query(Payment).get(id)
    
    def get_all(self):
        return self.session.query(Payment).all()
    
    def remove(self, id):
        payment = self.session.query(Payment).get(id)
        self.session.delete(payment)
    
    def add(self, customer_id, card_type, card_number):
        payment = Payment()
        payment.customer_id = customer_id
        payment.card_type = card_type
        payment.card_number = card_number
        self.session.add(payment)

    def add_from_csv(self, columns, values):
        payment = Payment()
        payment.from_csv(columns, values)
        self.session.add(payment)


class AccessCartManager(CartManager):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id):
        return self.session.query(Cart).get(id)
    
    def get_all(self):
        return self.session.query(Cart).all()
    
    def remove(self, id):
        cart = self.session.query(Cart).get(id)
        self.session.delete(cart)
    
    def add(self, number_of_products, total):
        cart = Cart()
        cart.number_of_products = number_of_products
        cart.total = total
        self.session.add(cart)

    def add_from_csv(self, columns, values):
        cart = Cart()
        cart.from_csv(columns, values)
        self.session.add(cart)


class AccessSellerManager(SellerManager):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id):
        return self.session.query(Seller).get(id)
    
    def get_all(self):
        return self.session.query(Seller).all()
    
    def remove(self, id):
        seller = self.session.query(Seller).get(id)
        self.session.delete(seller)
    
    def add(self, name):
        seller = Seller()
        seller.name = name
        self.session.add(name)

    def add_from_csv(self, columns, values):
        seller = Seller()
        seller.from_csv(columns, values)
        self.session.add(seller)
