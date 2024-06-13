import collections
from flask import Blueprint, jsonify, request, g
from models.data import get_all_data, get_by_id, add_data, update_data, delete_data, get_by_user_id
from middleware.auth import token_required

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

@data_bp.route('/list/<int:user_id>', methods=['GET'])
@token_required
def bookmark_jobs(user_id):
    data = get_all_data()
    filtered_data = [entry for entry in data if entry['created_by'] == user_id]
    return jsonify({
        'Result' : filtered_data
    })

@data_bp.route('/', methods=['POST'])
@token_required
def create_data():
    new_data = request.get_json()
    new_data['created_by'] = g.user_id
    employer_name = new_data.get('employer_name')
    job_naics_name = new_data.get('job_naics_name')
    if add_data(new_data):
        return jsonify({
            'employer_name' : employer_name,
            'job_naics_name' : job_naics_name,
            'message' : 'Berhasil Menambahkan Data'
        }), 200
    else:
        return jsonify({
            'Error' : 'Error Saat penambahan data!'
        }), 400
    
@data_bp.route('/list/<int:id>', methods=['DELETE'])
@token_required
def remove_data(id):
    if delete_data(id):
        return jsonify({
            'Message' : 'Data Berhasil dihapus'
        }), 200
    else:
        return jsonify({
            'Error' : 'Data gagal dihapus'
        }), 400


