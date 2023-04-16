from flask import Flask, render_template, make_response, jsonify, request
from src.executeQuerys import querysView
import sqlite3
from src.Consultas import *
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

# GET
@app.route('/get/<tableName>')
def getTable(tableName):
    return GetTable(tableName)


@app.route('/get/<tableName>/<idObject>')
def getTablebyID(tableName, idObject):
    return GetTableByID(tableName, idObject)


@app.route('/getH/Cliente')
def getActiveClientes():
    return GetActiveClientes()

@app.route('/getH/Reparto')
def getActiveRepartos():
    return GetActiveRepartos()

@app.route('/getH/Repartidor')
def getActiveRepartidores(): 
    return GetActiveRepartidores()

# ALTAS
@app.route('/post/upCliente', methods=['GET', 'POST'])
def postClient():
    altaCliente()
    return jsonify("Data OK")


@app.route('/post/upRepartidor', methods=['GET', 'POST'])
def postRepartidor():
    altaRepartidor()
    return jsonify("Data OK")


@app.route('/post/upReparto', methods=['GET', 'POST'])
def postReparto():
    altaReparto()
    return jsonify("Data OK")

@app.route('/post/upLineaReparto', methods=['GET', 'POST'])
def postLineaReparto():
    altaLineaReparto()
    return jsonify("Data OK")


@app.route('/post/upZona', methods=['GET', 'POST'])
def postZona():
    altaZona()
    return jsonify("Data OK")

@app.route('/post/upHistorico', methods=['GET', 'POST'])
def postHistorico():
    altaHistorico()
    return jsonify("Data OK")

# MODIFICACIONES
@app.route('/update/modCliente', methods=['PUT'])
def updateCliente():
    modCliente()
    return jsonify("Data OK")


@app.route('/update/modRepartidor', methods=['PUT'])
def updateRepartidor():
    modRepartidor()
    return jsonify("Data OK")


@app.route('/update/modReparto', methods=['PUT'])
def updateReparto():
    modReparto()
    return jsonify("Data OK")

@app.route('/update/modLineaReparto', methods=['PUT'])
def updateLineaReparto():
    modLineaReparto()
    return jsonify("Data OK")


@app.route('/update/modZona', methods=['PUT'])
def updateZona():
    modZona()
    return jsonify("Data OK")

# BAJAS
@app.route('/delete/delCliente', methods=['PUT'])
def delCliente():
    bajaCliente()
    return jsonify("Data OK")


@app.route('/delete/delRepartidor', methods=['PUT'])
def delRepartidor():
    bajaRepartidor()
    return jsonify("Data OK")


@app.route('/delete/delReparto', methods=['PUT'])
def delReparto():
    bajaReparto()
    return jsonify("Data OK")

@app.route('/habilita/Reparto', methods=['PUT'])
def habiReparto():
    habReparto()
    return jsonify("Data OK")

@app.route('/habilita/Repartidor', methods=['PUT'])
def habiRepartidor():
    habRepartidor()
    return jsonify("Data OK")

@app.route('/habilita/Cliente', methods=['PUT'])
def habiCliente():
    habCliente()
    return jsonify("Data OK")

@app.route('/delete/delLineaReparto', methods=['DELETE'])
def delLineaReparto():
    bajaLineaReparto()
    return jsonify("Data OK")

# CONSULTAS ESPECIFICAS
@app.route('/getH/ClienteZDesc')
def ClienteHZDesc():
    return ClienteDZDesc()

@app.route('/getD/ClienteZDesc')
def ClienteDZDesc():
    return ClienteDZDesc()


@app.route('/get/ClienteZDesc/<idObject>')
def ClienteZDescID(idObject):
    return ClienteZDescID()

@app.route('/get/ZonaxCliente/<idObject>')
def ZonaxCliente(idObject):
    return ZonaxCliente()


@app.route('/get/RepartoxLineaReparto/<idObject>')
def RepartoxLineaReparto(idObject):
    return RepartoxLineaReparto()

@app.route('/getH/RepartoTotal')
def RepartohTotal():
    return RepartohTotal()

@app.route('/getD/RepartoTotal')
def RepartoDTotal():
    return RepartoDTotal()

@app.route('/get/LineasRepartoCliente/<idCliente>')
def LineasRepartoCliente(idCliente):
    return LineasRepartoCliente()

@app.route('/get/RepartoTotal/<idObject>')
def RepartoTotalxId(idObject):
   return RepartoTotalxId

@app.route('/get/ClientesFaltantes/<idz>/<idr>')
def ClientesFaltantes(idz,idr):
    return ClientesFaltantes()

@app.route('/get/RepartosRepartidor/<idObject>')
def RepartosRepartidor(idObject):
    return RepartosRepartidor

@app.route('/get/RepartoHistoricoLinea/<idObject>')
def RepartoHistorico(idObject):
    return RepartoHistorico()

@app.route('/get/RepartoHistorico')
def RepartoFecha():
    return RepartoFecha()

# REPORTES
@app.route('/CantClientes')
def CantCli():
    return jsonify(ContadorClientes())


@app.route('/CantZonas')
def CantZon():
    return jsonify(ContadorZonas())


@app.route('/CantRepartidores')
def CantRepartidor():
    return jsonify(ContadorRepartidores())


@app.route('/CantRepartos')
def CantRepartos():
    return jsonify(ContadorRepartos())


@app.route('/CantBidones12')
def CantBidones12():
    return jsonify(ContadorBidones12())


@app.route('/CantBidones20')
def CantBidones20():
    return jsonify(ContadorBidones20())


@app.route('/CantSoda')
def CantSoda():
    return jsonify(ContadorSoda())
