from flask import Blueprint, jsonify

mobile_api = Blueprint('api', __name__, url_prefix='/api')


@mobile_api.route('/')
def index():
    return jsonify([])
