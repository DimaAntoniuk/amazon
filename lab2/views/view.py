from flask import Blueprint

request_api = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return request_api