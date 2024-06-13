import os
import jwt
from dotenv import load_dotenv
from flask import jsonify

load_dotenv()

SK = os.getenv('SECRET_KEY')

def encode_jwt(user_id):
    payload = {
        'sub': user_id
    }
    token = jwt.encode(payload, SK, algorithm="HS256")
    print(f"Result Token Login : {token}")
    print(f"Secret Key : {SK}")
    return token

def decode_jwt(token):
    try:
        print(f"Secret Key : {SK}")
        print(f"Decoding Token : {token}")
        payload = jwt.decode(token, SK, algorithms=["HS256"])
        print(f"Decode Payload : {payload}")
        return payload['sub']
        # return 'Berhasil Masuk'
    except jwt.ExpiredSignatureError:
        print("Token Expired")
        return 'Token Has Expired'
    except jwt.InvalidTokenError:
        print("Result : Token Invalid")
        return 'Invalid Token'