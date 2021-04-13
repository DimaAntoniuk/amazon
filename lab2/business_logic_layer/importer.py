import CSV

class Importer:
    def __init__(self, group_manager, subgroup_manager, seller_manager,
                       product_manager, cart_manager, customer_manager,
                       payment_manager):
        self.group_manager = group_manager
        self.subgroup_manager = subgroup_manager
        self.seller_manager = seller_manager
        self.product_manager = product_manager
        self.cart_manager = cart_manager
        self.customer_manager = customer_manager
        self.payment_manager = payment_manager

    def import_data(self, filename):
        parsed_csv = CSV.parse_csv(filename)
        group_columns, group_datalist = parsed_csv['group']
        for group_data in group_datalist:
            self.group_manager.add_from_csv(
                group_columns, group_data)
        
        subgroup_columns, subgroup_datalist = parsed_csv['subgroup']
        for subgroup_data in subgroup_datalist:
            self.subgroup_manager.add_from_csv(
                subgroup_columns, subgroup_data)
        
        seller_columns, seller_datalist = parsed_csv['seller']
        for seller_data in seller_datalist:
            self.seller_manager.add_from_csv(
                seller_columns, seller_data)

        product_columns, product_datalist = parsed_csv['product']
        for product_data in product_datalist:
            self.product_manager.add_from_csv(
                product_columns, product_data)

        product_columns, product_datalist = parsed_csv['product']
        for product_data in product_datalist:
            self.product_manager.add_from_csv(
                product_columns, product_data)
        
        customer_columns, customer_datalist = parsed_csv['customer']
        for customer_data in customer_datalist:
            self.customer_manager.add_from_csv(
                customer_columns, customer_data)
        
        payment_columns, payment_datalist = parsed_csv['payment']
        for payment_data in payment_datalist:
            self.payment_manager.add_from_csv(
                payment_columns, payment_data)
        
