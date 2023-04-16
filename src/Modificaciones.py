from flask import request
from src.executeQuerys import executeQuery

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
    idz = request.form.get('zona')       
    executeQuery("UPDATE Reparto SET idZona = ?, idRepartidor = ?, dia= ? WHERE idReparto = ?", (idz,idr,dia,idReparto2,) )
      
def modLineaReparto():
    idlr = request.form.get('idLineaReparto')
    idc = request.form.get('idCliente')
    idr = request.form.get('idReparto')       
    com12 = request.form.get('com12')
    com20 = request.form.get('com20')
    comSoda = request.form.get('comSoda')
    pago = request.form.get('pago')
    fiado = request.form.get('fiado')
    dev12 = request.form.get('dev12')
    dev20 = request.form.get('dev20')
    devSoda = request.form.get('devSoda')      
    executeQuery("UPDATE Reparto SET idCliente = ?, idReparto = ?, com12= ?, com20= ?, comSoda= ?, pago= ?, fiado= ?, dev12= ?, dev20= ? , devSoda= ?  WHERE idReparto = ?", (idc,idr,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,idlr,))

def modZona():
    idZona2 = request.form.get('idZona')
    descripcion = request.form.get('descripcion')             
    executeQuery("UPDATE Zona SET descripcion = ? WHERE idZona = ?", (descripcion.capitalize(),idZona2,) )
    
