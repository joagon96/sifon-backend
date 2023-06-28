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
@token_required
def getTable(tableName):
    return GetTable(tableName)

@app.route('/get/<tableName>/<idObject>')
def getTablebyID(tableName, idObject):
    return GetTableByID(tableName, idObject)

@app.route('/getH/Cliente')
def getActiveClientes():
    return GetActiveClientes()

@app.route('/getH/Zona')
def getActiveZonas():
    return GetActiveZonas()

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

@app.route('/update/deuda', methods=['PUT'])
def updateDeuda():
    modDeuda()
    return jsonify("Data OK")

@app.route('/update/producto', methods=['PUT'])
def updateProducto():
    modProducto()
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

@app.route('/finalizar/reparto/<idReparto>', methods=['PUT'])
def finReparto(idReparto):
    FinalizarReparto(idReparto)
    return jsonify("Data OK")


# BAJAS
@app.route('/delete/delCliente', methods=['PUT'])
def delCliente():
    bajaCliente()
    return jsonify("Data OK")

@app.route('/delete/delZona', methods=['PUT'])
def delZona():
    bajaZona()
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
def clienteHZDesc():
    return ClienteHZDesc()

@app.route('/getD/ClienteZDesc')
def clienteDZDesc():
    return ClienteDZDesc()

@app.route('/get/ClienteZDesc/<idObject>')
def clienteZDescID(idObject):
    return ClienteZDescID(idObject)

@app.route('/get/ZonaxCliente/<idObject>')
def zonaxCliente(idObject):
    return ZonaxCliente(idObject)

@app.route('/get/RepartoxLineaReparto/<idObject>')
def repartoxLineaReparto(idObject):
    return RepartoxLineaReparto(idObject)

@app.route('/getH/RepartoTotal')
def repartohTotal():
    return RepartohTotal()

@app.route('/getD/RepartoTotal')
def repartoDTotal():
    return RepartoDTotal()

@app.route('/get/LineaRepartoTotal/<idObject>')
def lineaRepartoTotal(idObject):
    return LineaRepartoTotal(idObject)

@app.route('/get/LineasRepartoCliente/<idCliente>')
def lineasRepartoCliente(idCliente):
    return LineasRepartoCliente(idCliente)

@app.route('/get/RepartoTotal/<idObject>')
def repartoTotalxId(idObject):
   return RepartoTotalxId(idObject)

@app.route('/get/ClientesFaltantes/<idz>/<idr>')
def clientesFaltantes(idz,idr):
    return ClientesFaltantes(idz, idr)

@app.route('/get/RepartosRepartidor/<idObject>')
def repartosRepartidor(idObject):
    return RepartosRepartidor

@app.route('/get/RepartoHistoricoLinea/<idObject>')
def repartoHistorico(idObject):
    return RepartoHistorico(idObject)

@app.route('/get/RepartoHistorico')
def repartoFecha():
    return RepartoFecha()

@app.route('/historico/lineas/<idHistorico>')
def historicoLineaReparto(idHistorico):
    return HistoricoLineaReparto(idHistorico)

@app.route('/search/historico', methods=['POST'])
def buscarHistorico():
    return BuscarHistorico()

@app.route('/resumen/reparto/<idReparto>', methods=['GET'])
def resumenReparto(idReparto):
    return ResumenReparto(idReparto)

@app.route('/resumen/historico/<idHistorico>', methods=['GET'])
def resumenHistorico(idHistorico):
    return ResumenHistorico(idHistorico)


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

@app.route('/CantPago')
def contadorPagos():
    return jsonify(ContadorPagos())

@app.route('/CantFiado')
def contadorFiados():
    return jsonify(ContadorFiados())

@app.route('/CantHistorico')
def contadorHistoricps():
    return jsonify(ContadorHistoricos())
