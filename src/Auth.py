from flask import request, jsonify
from flask_bcrypt import Bcrypt, check_password_hash
from flask_login import login_user, current_user,logout_user
from src.executeQuerys import executeQuery
from src.User import *

bcrypt = Bcrypt()

def Register():
    usuario = request.form.get('usuario')
    input_pwd = request.form.get('contrasena')
    pwd = bcrypt.generate_password_hash(input_pwd)
    executeQuery("INSERT INTO Usuario(usuario,password_hash, role) VALUES(?,?,?)",(usuario, pwd,"admin",))
    return jsonify("OK")

def Login():
    input_pwd = request.form.get('contrasena')
    user = User.getByUsername(request.form.get('usuario'))
    if user is not None and check_password_hash(user.password, input_pwd):
        login_user(user)
        return jsonify(user.role)
    else:
        return jsonify("Los datos ingresados son incorrectos")
    
def Logout():
    logout_user()
    return jsonify("Sesion finalizada")

def CurrentUser():
    return jsonify(current_user.username)