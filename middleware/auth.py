from functools import wraps
from flask import request, jsonify, g
from utils.jwt_utils import decode_jwt

def token_required(f):
    @wraps(f)
    def decorated_function(*agrs, **kwagrs):
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({
                'Error' : 'Token Is Missing',
            }), 401
        token = token.split(" ")[1] if " " in token else token
        print(f"Extracted Token : {token}")
        try:
            user_id = decode_jwt(token)
            if isinstance(user_id, str):
                return jsonify({
                    'Token' : token,
                    'Message' : user_id,
                })
            g.user_id = user_id
        except Exception as e:
            return jsonify({
                'Token' : token,
                'Error' : str(e)
            }), 401
        return f(*agrs, **kwagrs)
    return decorated_function