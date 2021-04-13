from models.models import Base, Product, Subgroup, Group, Customer,\
                          Payment, Cart, Seller
from business_logic_layer.manager import BusinessGroupManager,\
    BusinessSubgroupManager, BusinessSellerManager, BusinessProductManager,\
    BusinessCartManager, BusinessCustomerManager, BusinessPaymentManager
from data_access_layer.manager import AccessGroupManager,\
    AccessSubgroupManager, AccessSellerManager, AccessProductManager,\
    AccessCartManager, AccessCustomerManager, AccessPaymentManager
from views.view import View
from business_logic_layer.importer import Importer
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

    
SQLALCHEMY_DATABASE = 'D:/study/soft_doc/lab2/database/amazon.db'

def main():
    engine = create_engine('sqlite:///' + SQLALCHEMY_DATABASE)
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:    
        access_group_manager = AccessGroupManager(session)
        access_subgroup_manager = AccessSubgroupManager(session)
        access_seller_manager = AccessSellerManager(session)
        access_product_manager = AccessProductManager(session)
        access_cart_manager = AccessCartManager(session)
        access_customer_manager = AccessCustomerManager(session)
        access_payment_manager = AccessPaymentManager(session)

        business_group_manager = BusinessGroupManager(access_group_manager)
        business_subgroup_manager = BusinessSubgroupManager(access_subgroup_manager)
        business_seller_manager = BusinessSellerManager(access_seller_manager)
        business_product_manager = BusinessProductManager(access_product_manager)
        business_cart_manager = BusinessCartManager(access_cart_manager)
        business_customer_manager = BusinessCustomerManager(access_customer_manager)
        business_payment_manager = BusinessPaymentManager(access_payment_manager)

        # importer = Importer(
        #     group_manager=access_group_manager,
        #     subgroup_manager=access_subgroup_manager,
        #     seller_manager=access_seller_manager,
        #     product_manager=access_product_manager,
        #     cart_manager=access_cart_manager,
        #     customer_manager=access_customer_manager,
        #     payment_manager=access_payment_manager)
        
        # importer.import_data('generated_data.csv')
        # session.commit()
        
        print('Groups')
        for group in business_group_manager.get_all_groups():
            print(group)
        print('Subgroup')
        for subgroup in business_subgroup_manager.get_all_subgroups():
            print(subgroup)
        print('Seller')
        for seller in business_seller_manager.get_all_sellers()[:10]:
            print(seller)
        print('Product')
        for product in business_product_manager.get_all_products()[:10]:
            print(product)
        print('Cart')
        for cart in business_cart_manager.get_all_carts()[:10]:
            print(cart)
        print('Customer')
        for customer in business_customer_manager.get_all_customers()[:10]:
            print(customer)
        print('Payment')
        for payment in business_payment_manager.get_all_payments()[:10]:
            print(payment)


if __name__ == '__main__':
    main()