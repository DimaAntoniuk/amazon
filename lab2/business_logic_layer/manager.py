import interfaces
from models import Product, Subgroup, Group, Customer, Payment, Cart, Seller


class BussinessProductManager(ProductManager):
    def __init__(self, data_access_manager):
        self.data_access_manager = data_access_manager
    def get_product_by_id(self, id):
        return self.data_access_manager.get_by_id(id)
    def get_all_products(self):
        return self.data_access_manager.get_all()
    def remove_product(self, id):
        return self.data_access_manager.remove(id)
    def add_product(self, data):
        return self.data_access_manager.add(data)


class BussinessSubgroupManager(SubgroupManager):
    def __init__(self, data_access_manager):
        self.data_access_manager = data_access_manager
    def get_subgroup_by_id(self, id):
        return self.data_access_manager.get_by_id(id)
    def get_all_subgroups(self):
        return self.data_access_manager.get_all()
    def remove_subgroup(self, id):
        return self.data_access_manager.remove(id)
    def add_subgroup(self, data):
        return self.data_access_manager.add(data)


class BussinessGroupManager(GroupManager):
    def __init__(self, data_access_manager):
        self.data_access_manager = data_access_manager
    def get_group_by_id(self, id):
        return self.data_access_manager.get_by_id(id)
    def get_all_groups(self):
        return self.data_access_manager.get_all()
    def remove_group(self, id):
        return self.data_access_manager.remove(id)
    def add_group(self, data):
        return self.data_access_manager.add(data)


class BussinessCustomerManager(CustomerManager):
    def __init__(self, data_access_manager):
        self.data_access_manager = data_access_manager
    def get_customer_by_id(self, id):
        return self.data_access_manager.get_by_id(id)
    def get_all_customers(self):
        return self.data_access_manager.get_all()
    def remove_customer(self, id):
        return self.data_access_manager.remove(id)
    def add_customer(self, data):
        return self.data_access_manager.add(data)


class BussinessPaymentManager(PaymentManager):
    def __init__(self, data_access_manager):
        self.data_access_manager = data_access_manager
    def get_payment_by_id(self, id):
        return self.data_access_manager.get_by_id(id)
    def get_all_payments(self):
        return self.data_access_manager.get_all()
    def remove_payment(self, id):
        return self.data_access_manager.remove(id)
    def add_payment(self, data):
        return self.data_access_manager.add(data)


class BussinessCartManager(CartManager):
    def __init__(self, data_access_manager):
        self.data_access_manager = data_access_manager
    def get_cart_by_id(self, id):
        return self.data_access_manager.get_by_id(id)
    def get_all_carts(self):
        return self.data_access_manager.get_all()
    def remove_cart(self, id):
        return self.data_access_manager.remove(id)
    def add_cart(self, data):
        return self.data_access_manager.add(data)


class BussinessSellerManager(SellerManager):
    def __init__(self, data_access_manager):
        self.data_access_manager = data_access_manager
    def get_seller_by_id(self, id):
        return self.data_access_manager.get_by_id(id)
    def get_all_sellers(self):
        return self.data_access_manager.get_all()
    def remove_seller(self, id):
        return self.data_access_manager.remove(id)
    def add_seller(self, data):
        return self.data_access_manager.add(data)