from flask import request, jsonify, current_app
import jwt
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from src.executeQuerys import executeQuery, getQueryData


def Register():
    usuario = request.form.get('username')
    input_pwd = request.form.get('password')
    pwd = generate_password_hash(input_pwd, method='sha256')
    executeQuery("INSERT INTO Usuario(usuario,password_hash, role) VALUES(?,?,?)",
                 (usuario, pwd, "admin",))
    return jsonify("OK")


def Login():
    input_pwd = request.form.get('password')
    username = request.form.get('username')
    data = getQueryData(
        "SELECT id,usuario,password_hash,role FROM Usuario WHERE usuario = ?", (username,))
    if len(data) > 0 and check_password_hash(data[0]['password_hash'], input_pwd):
        token = jwt.encode({
            'user': username,
            'role': data[0]['role']
        }, current_app.config['SECRET_KEY'])
        return jsonify({"token": token, "username": username, "role": data[0]['role']})
    else:
        return jsonify({"error": "Invalid credentials"}), 401


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user_data = getQueryData(
                "SELECT id,usuario,password_hash,role FROM Usuario WHERE usuario = ?", (data['user'],))
            if len(user_data) == 0:
                raise RuntimeError('User not found')
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            return jsonify(invalid_msg), 401

    return _verify


def CurrentUser():
    auth_headers = request.headers.get('Authorization', '').split()
    token = auth_headers[1]
    data = jwt.decode(
        token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    return jsonify({"username": data['user'], "role": data['role']})
