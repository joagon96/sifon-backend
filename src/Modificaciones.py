from flask import Flask, render_template, jsonify, request
import json
from src.executeQuerys import querysView
from src.executeQuerys import executeQuery
import sqlite3

def modCliente():
    with sqlite3.connect("sifono_db.db") as con:
            idCliente2 = request.form.get('idCliente')
            name = request.form.get('nombreApellido')       
            dom = request.form.get('domicilio')
            tel = request.form.get('telefono')
            idz = request.form.get('idZona') 
            #con.row_factory = sqlite3.Row
            c = con.cursor()        
            c.execute("UPDATE Cliente SET idZona = ?, nomapeCli = ?, domicilio = ?, telefonoCli = ? WHERE idCliente = ?", (idz, name.capitalize(), dom.capitalize(), tel, idCliente2,) )
            con.commit()
    con.close()

def modRepartidor():
    with sqlite3.connect("sifono_db.db") as con:
        idRepartidor2 = request.form.get('idRepartidor')
        name = request.form.get('nombreApellido')       
        tel = request.form.get('telefono')
        #con.row_factory = sqlite3.Row
        c = con.cursor()        
        c.execute("UPDATE Repartidor SET nomapeRep = ?, telefonoRep = ? WHERE idRepartidor = ?", (name.capitalize(),tel.capitalize(),idRepartidor2,) )
        con.commit()
    con.close()

def modReparto():
    with sqlite3.connect("sifono_db.db") as con:
        idReparto2 = request.form.get('idReparto')       
        idr = request.form.get('idRepartidor')
        dia = request.form.get('dia')
        idz = request.form.get('zona')
        #con.row_factory = sqlite3.Row
        c = con.cursor()        
        c.execute("UPDATE Reparto SET idZona = ?, idRepartidor = ?, dia= ? WHERE idReparto = ?", (idz,idr,dia,idReparto2,) )
        con.commit()
    con.close()
      
def modLineaReparto():
    with sqlite3.connect("sifono_db.db") as con:
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
        #con.row_factory = sqlite3.Row
        c = con.cursor()        
        c.execute("UPDATE Reparto SET idCliente = ?, idReparto = ?, com12= ?, com20= ?, comSoda= ?, pago= ?, fiado= ?, dev12= ?, dev20= ? , devSoda= ?  WHERE idReparto = ?", (idc,idr,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,idlr,))
        con.commit()
    con.close()

def modZona():
    with sqlite3.connect("sifono_db.db") as con:
        idZona2 = request.form.get('idZona')
        descripcion = request.form.get('descripcion')       
        #con.row_factory = sqlite3.Row
        c = con.cursor()        
        c.execute("UPDATE Zona SET descripcion = ? WHERE idZona = ?", (descripcion.capitalize(),idZona2,) )
        con.commit()
    con.close()
    
