from flask import Blueprint, jsonify, request
from models.user import get_all_user, get_user_by_id, user_register, user_login

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_data():
    data = get_all_user()
    return jsonify(data)

@user_bp.route('/<int:id>', methods=['GET'])
def get_data_id(id):
    user = get_user_by_id(id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'Error' : 'User Not Found'}), 404

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'Error' : 'Username or password is empty'}), 400
    if user_login(username, password):
        return jsonify({'username' : username,
                        'password' : password,
                        'message' : 'User berhasil login'}), 200
    else:
        return jsonify({'message' : 'User tidak ditemukan'})

@user_bp.route("/register", methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'Error' : 'Username or password is empty'}), 400
    if user_register(username, password):
        return jsonify({'username' : username,
                        'password' : password,
                        'message' : 'User Berhasil Registrasi'}), 200
    else:
        return jsonify({'message' : 'username already exists'}), 400

@user_bp.route("/logout", methods=['GET'])
def logout():
    return jsonify({"message" : "Route logout"})