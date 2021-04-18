# from models.models import Product
# from business_logic_layer.manager import BusinessProductManager
# from data_access_layer.manager import AccessProductManager
# from flask import jsonify, abort, request, Blueprint
# from models import db

# request_api = Blueprint('request_api', __name__)


# def get_blueprint():
#     """Return the blueprint for the main app module"""
#     return request_api

# access_product_manager = AccessProductManager(db.session)
# business_product_manager = BusinessProductManager(access_product_manager)

# @request_api.route('/request', methods=['GET'])
# def get_records():
#     return jsonify()


# @request_api.route('/request/<string:_id>', methods=['GET'])
# def get_record_by_id(_id):
#     if not :
#         abort(404)
#     return jsonify(BOOK_REQUESTS[_id])


# @request_api.route('/request', methods=['POST'])
# def create_record():
#     """Create a book request record
#     @param email: post : the requesters email address
#     @param title: post : the title of the book requested
#     @return: 201: a new_uuid as a flask/response object \
#     with application/json mimetype.
#     @raise 400: misunderstood request
#     """
#     if not request.get_json():
#         abort(400)
#     data = request.get_json(force=True)

#     if not data.get('email'):
#         abort(400)
#     if not validate_email(data['email']):
#         abort(400)
#     if not data.get('title'):
#         abort(400)

#     new_uuid = str(uuid.uuid4())
#     book_request = {
#         'title': data['title'],
#         'email': data['email'],
#         'timestamp': datetime.now().timestamp()
#     }
#     BOOK_REQUESTS[new_uuid] = book_request
#     # HTTP 201 Created
#     return jsonify({"id": new_uuid}), 201


# @request_api.route('/request/<string:_id>', methods=['PUT'])
# def edit_record(_id):
#     """Edit a book request record
#     @param email: post : the requesters email address
#     @param title: post : the title of the book requested
#     @return: 200: a booke_request as a flask/response object \
#     with application/json mimetype.
#     @raise 400: misunderstood request
#     """
#     if _id not in BOOK_REQUESTS:
#         abort(404)

#     if not request.get_json():
#         abort(400)
#     data = request.get_json(force=True)

#     if not data.get('email'):
#         abort(400)
#     if not validate_email(data['email']):
#         abort(400)
#     if not data.get('title'):
#         abort(400)

#     book_request = {
#         'title': data['title'],
#         'email': data['email'],
#         'timestamp': datetime.now().timestamp()
#     }

#     BOOK_REQUESTS[_id] = book_request
#     return jsonify(BOOK_REQUESTS[_id]), 200


# @request_api.route('/request/<string:_id>', methods=['DELETE'])
# def delete_record(_id):
#     """Delete a book request record
#     @param id: the id
#     @return: 204: an empty payload.
#     @raise 404: if book request not found
#     """
#     if _id not in BOOK_REQUESTS:
#         abort(404)

#     del BOOK_REQUESTS[_id]

#     return '', 204