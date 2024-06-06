from flask import Blueprint, jsonify, request
from models.data import get_all_data, get_by_id, create_data, update_data, delete_data

data_bp = Blueprint('data', __name__)

@data_bp.route('/', methods=['GET'])
def get_data():
    data = get_all_data()
    return jsonify(data)

@data_bp.route('/<int:id>', methods=['GET'])
def get_data_by_id(id):
    data = get_by_id(id)
    if data:
        return jsonify(data)
    else:
        return jsonify({'error' : 'data not found'}), 404

@data_bp.route('/create', methods=['GET'])
def create_data():
    return jsonify("Route Add Data")


