from models.models import Base, Product, Subgroup, Group, Customer,\
                          Payment, Cart, Seller
from business_logic_layer.manager import BusinessGroupManager,\
    BusinessSubgroupManager, BusinessSellerManager, BusinessProductManager,\
    BusinessCartManager, BusinessCustomerManager, BusinessPaymentManager
from data_access_layer.manager import AccessGroupManager,\
    AccessSubgroupManager, AccessSellerManager, AccessProductManager,\
    AccessCartManager, AccessCustomerManager, AccessPaymentManager
from business_logic_layer.importer import Importer
from flask import Flask, jsonify, make_response, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
# from flask_restplus import Api
from models import db

SQLALCHEMY_DATABASE = 'D:/study/soft_doc/lab2/database/amazon.db'

app = Flask(__name__)

def initialize_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + SQLALCHEMY_DATABASE
    db.init_app(flask_app)
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger-ui.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Custom-Amazon"
        }
    )
    flask_app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':
    initialize_app(app)
    request_api = Blueprint('request_api', __name__)
    app.register_blueprint(request_api)
    with app.app_context():
        # db.drop_all()
        # db.create_all()

        access_product_manager = AccessProductManager(db.session)
        business_product_manager = BusinessProductManager(access_product_manager)
        
        # importer = Importer(
        #     group_manager=access_group_manager,
        #     subgroup_manager=access_subgroup_manager,
        #     seller_manager=access_seller_manager,
        #     product_manager=access_product_manager,
        #     cart_manager=access_cart_manager,
        #     customer_manager=access_customer_manager,
        #     payment_manager=access_payment_manager)
        
        # importer.import_data('generated_data.csv')
        # db.session.commit()
        
    app.run()


@request_api.route('/request', methods=['GET'])
def get_records():
    # with app.app_context():
    #     return jsonify(business_product_manager.get_all_products()[:10])
    return 'text'


@request_api.route('/request/<string:_id>', methods=['GET'])
def get_record_by_id(_id):
    with app.app_context():
        if not business_product_manager.get_product_by_id(_id):
            abort(404)
        return jsonify(business_product_manager.get_product_by_id(_id))


@request_api.route('/request', methods=['POST'])
def create_record():
    if not request.get_json():
        abort(400)

    data = request.get_json(force=True)

    if not data.get('name'):
        abort(400)
    with app.app_context():
        return jsonify(business_product_manager.add_product(name=name)), 201


@request_api.route('/request/<string:_id>', methods=['PUT'])
def edit_record(_id):
    with app.app_context():
        if not business_product_manager.get_product_by_id(_id):
            abort(404)

        if not request.get_json():
            abort(400)
        data = request.get_json(force=True)

        if not data.get('name'):
            abort(400)

        return jsonify(business_product_manager.edit_product(_id, data.get('name'))), 200


@request_api.route('/request/<string:_id>', methods=['DELETE'])
def delete_record(_id):
    with app.app_context():
        if not business_product_manager.get_product_by_id(_id):
            abort(404)

        business_product_manager.remove_product(_id)

    return '', 204