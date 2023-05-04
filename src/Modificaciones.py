from flask import request
from src.executeQuerys import executeQuery, getQueryData
from datetime import datetime

def modCliente():
    idCliente2 = request.form.get('idCliente')
    name = request.form.get('nombreApellido')       
    dom = request.form.get('domicilio')
    tel = request.form.get('telefono')
    idz = request.form.get('idZona')     
    executeQuery("UPDATE Cliente SET idZona = ?, nomapeCli = ?, domicilio = ?, telefonoCli = ? WHERE idCliente = ?", (idz, name.capitalize(), dom.capitalize(), tel, idCliente2,) )

def modRepartidor():
    idRepartidor2 = request.form.get('idRepartidor')
    name = request.form.get('nombreApellido')       
    tel = request.form.get('telefono')       
    executeQuery("UPDATE Repartidor SET nomapeRep = ?, telefonoRep = ? WHERE idRepartidor = ?", (name.capitalize(),tel.capitalize(),idRepartidor2,) )

def modReparto():
    idReparto2 = request.form.get('idReparto')       
    idr = request.form.get('idRepartidor')
    dia = request.form.get('dia')
    idz = request.form.get('idZona')   
    executeQuery("UPDATE Reparto SET idZona = ?, idRepartidor = ?, dia= ? WHERE idReparto = ?", (idz,idr,dia,idReparto2,) )
      
def modLineaReparto():
    idlr = request.form.get('idLR')
    idc = request.form.get('idCliente')
    idr = request.form.get('idReparto')
    est12 = request.form.get('est12')
    est20 = request.form.get('est20')
    estSoda = request.form.get('estSoda')       
    com12 = request.form.get('com12')
    com20 = request.form.get('com20')
    comSoda = request.form.get('comSoda')
    pago = request.form.get('pago')
    fiado = request.form.get('fiado')
    dev12 = request.form.get('dev12')
    dev20 = request.form.get('dev20')
    devSoda = request.form.get('devSoda')
    observacion = str(request.form.get('observacion'))
    executeQuery("UPDATE LineaReparto SET idCliente = ?, idReparto = ?, est12= ?, est20= ?, estSoda= ?, com12= ?, com20= ?, comSoda= ?, pago= ?, fiado= ?, dev12= ?, dev20= ? , devSoda= ?, observacion =?  WHERE idLR = ?", (idc,idr,est12,est20,estSoda,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,observacion,idlr,))

def modZona():
    idZona2 = request.form.get('idZona')
    descripcion = request.form.get('descripcion')             
    executeQuery("UPDATE Zona SET descripcion = ? WHERE idZona = ?", (descripcion.capitalize(),idZona2,) )
    
def FinalizarReparto(idReparto):
    lineasReparto = getQueryData("SELECT * FROM Reparto NATURAL JOIN LineaReparto NATURAL JOIN Cliente NATURAL JOIN Repartidor NATURAL JOIN Zona WHERE Reparto.idReparto=? ", (idReparto,))
    fecha = datetime.now().strftime("%Y-%m-%d")       
    idh = executeQuery("INSERT INTO Historico(fecha,repartidor,zona,dia) VALUES (?,?,?,?)",(
        fecha,
        lineasReparto[0]['nomapeRep'],
        lineasReparto[0]['descripcion'],
        lineasReparto[0]['dia'],
        ))
    for linea in lineasReparto:
        executeQuery("INSERT INTO HistoricoLinea(idHistorico,cliente,domicilio,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,observacion) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(
            idh,
            linea['nomapeCli'],
            linea['domicilio'],
            linea['com12'],
            linea['com20'],
            linea['comSoda'],
            linea['pago'],
            linea['fiado'],
            linea['dev12'],
            linea['dev20'],
            linea['devSoda'],
            linea['observacion'],
            ))
    executeQuery("UPDATE LineaReparto SET com12= ?, com20= ?, comSoda= ?, pago= ?, fiado= ?, dev12= ?, dev20= ? , devSoda= ?, observacion =?  WHERE idReparto = ?", (0,0,0,0,0,0,0,0,"",idReparto,))