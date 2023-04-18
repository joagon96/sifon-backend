from flask import Flask, jsonify
from flask_cors import CORS
from src.executeQuerys import querysView
from src.Auth import *
from src.Consultas import *
from src.Altas import *
from src.Modificaciones import *
from src.Bajas import *
from src.ReportesGeneral import *

app = Flask(__name__)
CORS(app)
app.register_blueprint(querysView)


@app.route('/')
@app.route('/index')

#AUTH
@app.route('/register', methods=['POST'])
def register():
    return Register()

@app.route('/login', methods=['POST'])
def login():
    return Login()

@app.route('/currentUser')
@token_required
def currentUser():
    return CurrentUser()


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
