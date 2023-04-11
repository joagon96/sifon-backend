from flask import Flask, render_template, make_response, jsonify, request, Response
import json
from src.executeQuerys import querysView
from src.executeQuerys import executeQuery
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from src.Altas import *
from src.Modificaciones import *
from src.Bajas import *
from src.ReportesGeneral import *
from flask_cors import CORS
from Auth import auth
# from passlib.apps import custom_app_context as pwd_context
# from itsdangerous import (TimedJSONWebSignatureSerializer
#                           as Serializer, BadSignature, SignatureExpired)
app = Flask(__name__)
CORS(app)
app.register_blueprint(querysView)
# #executeQuery('''INSERT INTO Cliente(nomape,domicilio,telefono) VALUES ("nano","mitre","345")''')
# # executeQuery('''CREATE TABLE "Cliente" (
# #  "idCliente" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# #  "idZona" INTEGER,
# #  "nomape" TEXT NOT NULL,
# #  "domicilio" TEXT NOT NULL,
# #  "telefono" INTEGER NOT NULL,
# #  FOREIGN KEY("idZona") REFERENCES "Zona"("idZona")
# # )''')

security = auth.AuthBraska()


@app.route('/')
@app.route('/index')
@auth.require_api_token
def index(userCurrent):
    if userCurrent:
        return jsonify({'nameUser' : userCurrent[1]})
    else:
        return make_response("Not logged")
    return render_template('index.html')

@app.route('/logout')
def logout():
    g.user = None
    return ('Logout', 401)

@app.route('/login')
def login():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
        return make_response('No se puede verificar usuario', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) 

    # find user
    with sqlite3.connect("sifono_db.db") as con:
        c = con.cursor()
        c.execute("SELECT * FROM Usuario WHERE usuario=?",(auth.username,))
        idUser, nameUser, passUser = c.fetchone()
    con.commit()
    con.close()
    
    passUser = passUser.encode('ascii','ignore')
    print(type(passUser), passUser.rstrip())
    print(type(auth.password), auth.password)
    
    if not idUser:
        return make_response('No se puede verificar usuario', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
    
    #if check_password_hash(user.password, auth.password):
    if (passUser == auth.password):
        token = security.encode(idUser)   
        return jsonify({'token': token})
    else:  
        return make_response('No se puede verificar usuario', 401, {'WWW-Authenticate' : 'Basic realm="Bad password"'})
    
    
# #HASH
# def hash_password(password):
#     with sqlite3.connect("sifono_db.db") as con:
#         c = con.cursor()
#         ph = pwd_context.encrypt(password)
#         c.execute("UPDATE Usuario SET password_hash = ?",(ph,))
#     c.close()
#     # self.password_hash = pwd_context.encrypt(password)

# def verify_password(password):
#     with sqlite3.connect("sifono_db.db") as con:
#         c = con.cursor()
#         ph = pwd_context.encrypt(password)
#         c.execute("SELECT password_hash FROM Usuario")
#         pw=c.fetchone()
#         return pwd_context.verify(password, pw)
#     c.close()


# #TOKEN AUTTHORIZATION
# def generate_auth_token(expiration = 600):
#     with sqlite3.connect("sifono_db.db") as con:
#         c = con.cursor()
#         s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
#         c.execute("SELECT id FROM Usuario")
#         return s.dumps({ 'id': self.id })
#     c.close()

# @staticmethod
# def verify_auth_token(token):
#     with sqlite3.connect("sifono_db.db") as con:
#         c = con.cursor()
#         s = Serializer(app.config['SECRET_KEY'])
#         try:
#             data = s.loads(token)
#         except SignatureExpired:
#             return None # valid token, but expired
#         except BadSignature:
#             return None # invalid token
#         user = c.execute("SELECT id FROM Usuario")
#         con.commit()
#         # user = User.query.get(data['id'])
#         return user
#     con.close()

# @app.route('/api/token')
# @auth.login_required
# def get_auth_token():
#     token = g.user.generate_auth_token()
#     return jsonify({ 'token': token.decode('ascii') })

# @auth.verify_password
# def verify_password(username_or_token, password):
#     # first try to authenticate by token
#     with sqlite3.connect("sifono_db.db") as con:
#         c = con.cursor()
#         user = Usuario.verify_auth_token(username_or_token)
#         if not user:
#             # try to authenticate with username/password
#             # user = User.query.filter_by(username = username_or_token).first()
#             c.execute("SELECT * FROM Usuario WHERE usuario=?",(username_or_token,))
#             user = c.fetchone()
#             if not user or not user.verify_password(password):
#                 return False
#         g.user = user
#         return True
#     con.close()

# GET
@app.route('/getH/Cliente')
def getHTable():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 1
        c.execute("select * from Cliente where habilitadoC=?",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getH/Reparto')
def getH2Table():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 1
        c.execute("select * from Reparto where habilitadoReparto=?",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getH/Repartidor')
def getH3Table():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 1
        c.execute("select * from Repartidor where habilitadoRep=?",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getD/Cliente')
def getDTable():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 0
        c.execute("select * from Cliente where habilitadoC=?",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getD/Reparto')
def getD2Table():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 0
        c.execute("select * from Reparto where habilitadoReparto=?",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getD/Repartidor')
def getD3Table():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 0
        c.execute("select * from Repartidor where habilitadoRep=?",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/<tableName>')
def getTable(tableName):
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute("select * from " + tableName)
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")


@app.route('/get/<tableName>/<idObject>')
def getTablebyID(tableName, idObject):
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        query = "SELECT * FROM "+tableName+" WHERE id"+tableName+"="+idObject
        print(query)
        c.execute(query)
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
            # list_temp.append({ rowsValues[0] : dictA})
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

# ALTAS
@app.route('/post/upCliente', methods=['GET', 'POST'])
def postClient():
    if request.method == 'GET':
        return jsonify("Dont use GET on this")
    else:
        altaCliente()
        return jsonify("Data OK")


@app.route('/post/upRepartidor', methods=['GET', 'POST'])
def postRepartidor():
    if request.method == 'GET':
        return jsonify("Dont use GET on this")
    else:
        altaRepartidor()
        return jsonify("Data OK")


@app.route('/post/upReparto', methods=['GET', 'POST'])
def postReparto():
    if request.method == 'GET':
        return jsonify("Dont use GET on this")
    else:
        altaReparto()
        return jsonify("Data OK")

@app.route('/post/upLineaReparto', methods=['GET', 'POST'])
def postLineaReparto():
    if request.method == 'GET':
        return jsonify("Dont use GET on this")
    else:
        altaLineaReparto()
        return jsonify("Data OK")


@app.route('/post/upZona', methods=['GET', 'POST'])
def postZona():
    if request.method == 'GET':
        return jsonify("Dont use GET on this")
    else:
        altaZona()
        return jsonify("Data OK")

@app.route('/post/upHistorico', methods=['GET', 'POST'])
def postHistorico():
    if request.method == 'GET':
        return jsonify("Dont use GET on this")
    else:
        altaHistorico()
        return jsonify("Data OK")

# MODIFICACIONES
@app.route('/update/modCliente', methods=['PUT'])
def updateCliente():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        modCliente()
        return jsonify("Data OK")


@app.route('/update/modRepartidor', methods=['PUT'])
def updateRepartidor():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        modRepartidor()
        return jsonify("Data OK")


@app.route('/update/modReparto', methods=['PUT'])
def updateReparto():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        modReparto()
        return jsonify("Data OK")

@app.route('/update/modLineaReparto', methods=['PUT'])
def updateLineaReparto():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        modLineaReparto()
        return jsonify("Data OK")


@app.route('/update/modZona', methods=['PUT'])
def updateZona():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        modZona()
        return jsonify("Data OK")
# BAJAS
@app.route('/delete/delCliente', methods=['PUT'])
def delCliente():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        bajaCliente()
        return jsonify("Data OK")


@app.route('/delete/delRepartidor', methods=['PUT'])
def delRepartidor():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        bajaRepartidor()
        return jsonify("Data OK")


@app.route('/delete/delReparto', methods=['PUT'])
def delReparto():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        bajaReparto()
        return jsonify("Data OK")

@app.route('/habilita/Reparto', methods=['PUT'])
def habiReparto():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        habReparto()
        return jsonify("Data OK")

@app.route('/habilita/Repartidor', methods=['PUT'])
def habiRepartidor():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        habRepartidor()
        return jsonify("Data OK")

@app.route('/habilita/Cliente', methods=['PUT'])
def habiCliente():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        habCliente()
        return jsonify("Data OK")


# @app.route('/delete/delZona', methods=['DELETE'])
# def delZona():
#     if request.method != 'DELETE':
#         return jsonify("Use DELETE on this")
#     else:
#         bajaZona()
#         return jsonify("Data OK")

@app.route('/delete/delLineaReparto', methods=['DELETE'])
def delLineaReparto():
    if request.method != 'DELETE':
        return jsonify("Use DELETE on this")
    else:
        bajaLineaReparto()
        return jsonify("Data OK")

@app.route('/delete/<tableName>')
def dropDatabase(tableName, methods=['DELETE']):
    with sqlite3.connect('sifono_db.db') as con:
        c = con.cursor()
        c.execute("delete from "+tableName)
        c.execute("update sqlite_sequence set seq=0 where name='"+tableName+"'")
        con.commit()
    con.close()
    return jsonify("I hope you know what are you doing...")

# CONSULTAS ESPECIFICAS


@app.route('/getH/ClienteZDesc')
def ClienteHZDesc():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 1
        c.execute("SELECT * FROM Cliente Natural JOIN Zona WHERE habilitadoC=? ORDER BY Cliente.nomapeCli ASC",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getD/ClienteZDesc')
def ClienteDZDesc():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 0
        c.execute("SELECT * FROM Cliente Natural JOIN Zona WHERE habilitadoC=? ORDER BY Cliente.nomapeCli ASC",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")


@app.route('/get/ClienteZDesc/<idObject>')
def ClienteZDescID(idObject):
    with sqlite3.connect("sifono_db.db") as con:
        c = con.cursor()
        c.execute(
            "SELECT * FROM Cliente NATURAL JOIN Zona WHERE Cliente.idCliente=?", (idObject,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/ZonaxCliente/<idObject>')
def ZonaxCliente(idObject):
    with sqlite3.connect("sifono_db.db") as con:
        c = con.cursor()
        c.execute(
            "SELECT * FROM Zona NATURAL JOIN Cliente WHERE Zona.idZona=? ORDER BY Cliente.nomapeCli ASC", (idObject,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")


@app.route('/get/RepartoxLineaReparto/<idObject>')
def RepartoxLineaReparto(idObject):
    with sqlite3.connect("sifono_db.db") as con:
        c = con.cursor()
        c.execute(
            "SELECT * FROM Reparto NATURAL JOIN LineaReparto NATURAL JOIN Cliente WHERE Reparto.idReparto=? ", (idObject,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getH/RepartoTotal')
def RepartohTotal():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 1
        c.execute(
            "SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Reparto.habilitadoReparto=? ORDER BY Repartidor.nomapeRep ASC",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/getD/RepartoTotal')
def RepartoDTotal():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 0
        c.execute(
            "SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Reparto.habilitadoReparto=? ORDER BY Repartidor.nomapeRep ASC",(hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/LineasRepartoCliente/<idCliente>')
def LineasRepartoCliente(idCliente):
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute(
            "SELECT * FROM Cliente NATURAL JOIN LineaReparto WHERE Cliente.idCliente=? ORDER BY Cliente.nomapeCli ASC",(idCliente,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/RepartoTotal/<idObject>')
def RepartoTotalxId(idObject):
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute(
            "SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Reparto.idReparto=? ORDER BY Repartidor.nomapeRep ASC",(idObject,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/ClientesFaltantes/<idz>/<idr>')
def ClientesFaltantes(idz,idr):
    with sqlite3.connect("sifono_db.db") as con:
        # idz = request.form.get('idZona')       
        # idr = request.form.get('idReparto')
        c = con.cursor()
        c.execute("SELECT * FROM LineaReparto WHERE idReparto=?",(idr,)) 
        aux = c.fetchall()
        print (aux)
        if (aux != []):       
            c.execute("SELECT * FROM Cliente NATURAL JOIN Zona WHERE Cliente.idZona=? AND Cliente.idCliente NOT IN (SELECT idCliente FROM LineaReparto WHERE idReparto= "+str(idr)+" ) ORDER BY Cliente.nomapeCli ",(idz,))  
            rows = c.fetchall()
            names = list(map(lambda x: x[0], c.description))
            list_temp = []
            for rowsValues in rows:
                dictA = {}
                for i, value in enumerate(rowsValues):
                    dictA[names[i]] = value
                list_temp.append(dictA)
            print(list_temp)
            return jsonify(list_temp)
        else:
            c.execute(
            "SELECT * FROM Cliente NATURAL JOIN Zona WHERE Cliente.idZona=? ORDER BY Cliente.nomapeCli", (idz,))  
            rows = c.fetchall()
            names = list(map(lambda x: x[0], c.description))
            list_temp = []
            for rowsValues in rows:
                dictA = {}
                for i, value in enumerate(rowsValues):
                    dictA[names[i]] = value
                list_temp.append(dictA)
            print(list_temp)
            return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/RepartosRepartidor/<idObject>')
def RepartosRepartidor(idObject):
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        hab = 1
        c.execute(
            "SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Repartidor.idRepartidor=? AND Reparto.habilitadoReparto=?",(idObject,hab,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/RepartoHistoricoLinea/<idObject>')
def RepartoHistorico(idObject):
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute(
            "SELECT * FROM Historico NATURAL JOIN Reparto NATURAL JOIN LineaReparto WHERE LineaReparto.idLineaReparto=?",(idObject,))
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

@app.route('/get/RepartoHistorico')
def RepartoFecha():
    with sqlite3.connect("sifono_db.db") as con:
        #con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute(
            "SELECT * FROM Historico NATURAL JOIN Reparto NATURAL JOIN Zona NATURAL JOIN Repartidor WHERE Historico.idReparto=Reparto.idReparto")
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        list_temp = []
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            list_temp.append(dictA)
        print(list_temp)
        return jsonify(list_temp)
    con.close()
    return jsonify("No data")

# REPORTES
@app.route('/CantClientes')
def CantCli():
    print(ContadorClientes())
    return jsonify(ContadorClientes())


@app.route('/CantZonas')
def CantZon():
    print(ContadorZonas())
    return jsonify(ContadorZonas())


@app.route('/CantRepartidores')
def CantRepartidor():
    print(ContadorRepartidores())
    return jsonify(ContadorRepartidores())


@app.route('/CantRepartos')
def CantRepartos():
    print(ContadorRepartos())
    return jsonify(ContadorRepartos())


@app.route('/CantBidones12')
def CantBidones12():
    print(ContadorBidones12())
    return jsonify(ContadorBidones12())


@app.route('/CantBidones20')
def CantBidones20():
    print(ContadorBidones20())
    return jsonify(ContadorBidones20())


@app.route('/CantSoda')
def CantSoda():
    print(ContadorSoda())
    return jsonify(ContadorSoda())
