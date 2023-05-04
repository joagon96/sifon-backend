from flask import jsonify, request
from src.executeQuerys import getQueryData

def GetTable(tableName):
    return jsonify(getQueryData("SELECT * FROM " + tableName))
        
def GetTableByID(tableName, idObject):
    return jsonify(getQueryData("SELECT * FROM "+tableName+" WHERE id"+tableName+"="+idObject))
     
def GetActiveClientes():
    hab = 1
    return jsonify(getQueryData("SELECT * FROM Cliente WHERE habilitadoC=?",(hab,)))

def GetActiveZonas():
    hab = 1
    return jsonify(getQueryData("SELECT * FROM Zona WHERE habilitado=?",(hab,)))
     
def GetActiveRepartos():
    hab = 1
    return jsonify(getQueryData("SELECT * FROM Reparto WHERE habilitadoReparto=?",(hab,)))


def GetActiveRepartidores():
    hab = 1
    return jsonify(getQueryData("SELECT * FROM Repartidor WHERE habilitadoRep=?",(hab,)))
    
def ClienteHZDesc():
    hab = 1
    return jsonify(getQueryData("SELECT * FROM Cliente Natural JOIN Zona WHERE habilitadoC=? ORDER BY Cliente.nomapeCli ASC",(hab,)))

def ClienteDZDesc():
    hab = 0
    return jsonify(getQueryData("SELECT * FROM Cliente Natural JOIN Zona WHERE habilitadoC=? ORDER BY Cliente.nomapeCli ASC",(hab,)))

def ClienteZDescID(idObject):
    return jsonify(getQueryData("SELECT * FROM Cliente NATURAL JOIN Zona WHERE Cliente.idCliente=?", (idObject,)))

def ZonaxCliente(idObject):
    return jsonify(getQueryData("SELECT * FROM Zona NATURAL JOIN Cliente WHERE Zona.idZona=? ORDER BY Cliente.nomapeCli ASC", (idObject,)))



def RepartoxLineaReparto(idObject):
    return jsonify(getQueryData("SELECT * FROM Reparto NATURAL JOIN LineaReparto NATURAL JOIN Cliente WHERE Reparto.idReparto=? ", (idObject,)))


def RepartohTotal():
    hab = 1
    return jsonify(getQueryData("SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Reparto.habilitadoReparto=? ORDER BY Repartidor.nomapeRep ASC",(hab,)))

def RepartoDTotal():
    hab = 0
    return jsonify(getQueryData("SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Reparto.habilitadoReparto=? ORDER BY Repartidor.nomapeRep ASC",(hab,)))


def LineasRepartoCliente(idCliente):
    return jsonify(getQueryData("SELECT * FROM Cliente NATURAL JOIN LineaReparto WHERE Cliente.idCliente=? ORDER BY Cliente.nomapeCli ASC",(idCliente,)))

def RepartoTotalxId(idObject):
    return jsonify(getQueryData("SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Reparto.idReparto=? ORDER BY Repartidor.nomapeRep ASC",(idObject,)))

def ClientesFaltantes(idz,idr):
    query = "SELECT * FROM Cliente NATURAL JOIN Zona WHERE Cliente.habilitadoC = 1 AND Cliente.idZona=? ORDER BY Cliente.nomapeCli"
    aux = getQueryData("SELECT * FROM LineaReparto WHERE idReparto=?",(idr,))
    if (aux != []):       
        query = "SELECT * FROM Cliente NATURAL JOIN Zona WHERE Cliente.habilitadoC = 1 AND Cliente.idZona=? AND Cliente.idCliente NOT IN (SELECT idCliente FROM LineaReparto WHERE idReparto= "+str(idr)+" ) ORDER BY Cliente.nomapeCli "
    return jsonify(getQueryData(query, (idz,)))

def RepartosRepartidor(idObject):
    hab = 1
    return jsonify(getQueryData("SELECT * FROM Reparto NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Repartidor.idRepartidor=? AND Reparto.habilitadoReparto=?",(idObject,hab,)))

def RepartoHistorico(idObject):
    return jsonify(getQueryData("SELECT * FROM Historico NATURAL JOIN Reparto NATURAL JOIN LineaReparto WHERE LineaReparto.idLineaReparto=?",(idObject,)))

def HistoricoLineaReparto(idObject):
    return jsonify(getQueryData("SELECT * FROM HistoricoLinea WHERE idHistorico=?",(idObject,)))

def RepartoFecha():
    return jsonify(getQueryData("SELECT * FROM Historico NATURAL JOIN Reparto NATURAL JOIN Zona NATURAL JOIN Repartidor WHERE Historico.idReparto=Reparto.idReparto"))

def LineaRepartoTotal(idObject):
    return jsonify(getQueryData("SELECT * FROM LineaReparto NATURAL JOIN Cliente WHERE LineaReparto.idLR=? ", (idObject,)))

def BuscarHistorico():
    zona = request.form.get('zona')       
    dia = request.form.get('dia')
    repartidor = request.form.get('repartidor')
    fecha = request.form.get('fecha')
    params = []
    values = []
    query = "SELECT * FROM Historico "
    if (zona):
        params.append("zona = ?")
        values.append(zona)
    if (dia):
        params.append("dia = ?")
        values.append(dia)
    if (repartidor):
        params.append("repartidor = ?")
        values.append(repartidor)
    if (fecha):
        params.append("fecha = ?")
        values.append(fecha)
    if (len(params) > 0 and len(values) > 0):
        separator = " AND "
        query += "WHERE " + separator.join(params)

    query += " ORDER BY idHistorico DESC"
    return jsonify(getQueryData(query, values))

