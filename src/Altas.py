from flask import request
from src.executeQuerys import executeQuery
from datetime import datetime

def altaCliente():
    name = request.form.get('nombreApellido')       
    dom = request.form.get('domicilio')
    tel = request.form.get('telefono')
    idz = request.form.get('idZona')
    hab = 1
    executeQuery("INSERT INTO Cliente(idZona,nomapeCli,domicilio,telefonoCli,habilitadoC) VALUES (?,?,?,?,?)",(idz, name.capitalize(),dom.capitalize(),tel,hab,))

def altaRepartidor():
    name = request.form.get('nombreApellido')       
    tel = request.form.get('telefono')
    hab = 1     
    executeQuery("INSERT INTO Repartidor(nomapeRep,telefonoRep,habilitadoRep) VALUES (?,?,?)",(name.capitalize(),tel,hab,))

def altaReparto():     
    idr = request.form.get('idRepartidor')
    dia = request.form.get('dia')
    idz = request.form.get('zona')
    hab = 1
    estado = 'pendiente'
    fechaCreacion = datetime.now()       
    executeQuery("INSERT INTO Reparto(idRepartidor,dia,habilitadoReparto,idZona,estado,fechaCreacion) VALUES (?,?,?,?,?,?)",(idr,dia,hab,idz,fechaCreacion,estado))

def altaLineaReparto():
    idc = request.form.get('idCliente')       
    idr = request.form.get('idReparto')
    co12 = request.form.get('com12')
    co20 = request.form.get('com20')
    coms = request.form.get('comSoda')
    pag = 0
    fia = 0
    de12 = 0
    de20 = 0
    deS = 0
    executeQuery("INSERT INTO LineaReparto(idCliente,idReparto,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda) VALUES (?,?,?,?,?,?,?,?,?,?)",(idc,idr,co12,co20,coms,pag,fia,de12,de20,deS,))

def altaZona():
    desc = request.form.get('descripcionZona')              
    executeQuery("INSERT INTO Zona(descripcion) VALUES (?)",(desc.capitalize(),))

def altaHistorico():
    idr = request.form.get('repartidor')   
    fech = request.form.get('fecha') 
    zona = request.form.get('zona')
    dia = request.form.get('dia')      
    executeQuery("INSERT INTO Historico(repartidor,fecha,zona,dia) VALUES (?,?,?,?)",(idr,fech,zona,dia,))

def altaHistoricoLinea():
    idh = request.form.get('idHistorico')
    cli = request.form.get('cliente')   
    domicilio = request.form.get('domicilio') 
    com12 = request.form.get('com12')
    com20 = request.form.get('com20')
    comSoda = request.form.get('comSoda')
    pago = request.form.get('pago')
    fiado = request.form.get('fiado')
    dev12 = request.form.get('dev12')
    dev20 = request.form.get('dev20')
    devSoda = request.form.get('devSoda')
    observacion = request.form.get('observacion')      
    executeQuery("INSERT INTO HistoricoLinea(idHistorico,cliente,domicilio,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,observacion) VALUES (?,?,?,?,?,?,?,]?,?,?,?,?)",(idh,cli,domicilio,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,observacion,))

def habCliente():
    idCliente2 = request.form.get('idCliente')       
    hab = 1      
    executeQuery("UPDATE Cliente SET habilitadoC=? WHERE idCliente = ?", (hab,idCliente2,) )

def habReparto():
    idReparto2 = request.form.get('idReparto')             
    hab = 1      
    executeQuery("UPDATE Reparto SET habilitadoReparto=? WHERE idReparto = ?", (hab,idReparto2,) )

def habRepartidor():
    idRepartidor2 = request.form.get('idRepartidor')             
    hab = 1     
    executeQuery("UPDATE Repartidor SET habilitadoRep=? WHERE idRepartidor = ?", (hab,idRepartidor2,))