from flask import Flask, render_template, jsonify, request
import json
from src.executeQuerys import querysView
from src.executeQuerys import executeQuery
import sqlite3

def altaCliente():
    with sqlite3.connect("sifono_db.db") as con:
        name = request.form.get('nombreApellido')       
        dom = request.form.get('domicilio')
        tel = request.form.get('telefono')
        idz = request.form.get('idZona')
        hab = 1
        c = con.cursor()        
        c.execute("INSERT INTO Cliente(idZona,nomapeCli,domicilio,telefonoCli,habilitadoC) VALUES (?,?,?,?,?)",(idz, name.capitalize(),dom.capitalize(),tel,hab,))
        con.commit()
    con.close()

def altaRepartidor():
    with sqlite3.connect("sifono_db.db") as con:
        name = request.form.get('nombreApellido')       
        tel = request.form.get('telefono')
        hab = 1
        c = con.cursor()        
        c.execute("INSERT INTO Repartidor(nomapeRep,telefonoRep,habilitadoRep) VALUES (?,?,?)",(name.capitalize(),tel,hab,))
        con.commit()
    con.close()

# def altaReparto():

#     with sqlite3.connect("sifono_db.db") as con:
#         idz = request.form.get('idZona')       
#         idr = request.form.get('idRepartidor')
#         dia = request.form.get('dia')
#         tupl = request.form.getlist('tupla')
#         #con.row_factory = sqlite3.Row
#         c = con.cursor()        
#         c.execute("INSERT INTO Reparto(idZona,idRepartidor,dia) VALUES (?,?,?)",(idz,idr,dia,))
#         con.commit()
#         c.execute("SELECT idReparto FROM Reparto ORDER BY idReparto DESC LIMIT 1")
#         idrep = c.fetchone()
#         print (idrep[0])
#         print ("zz",idrep)
#         co12 = 0
#         co20 = 0
#         coms = 0
#         pag = 0
#         fia = 0
#         de12 = 0
#         de20 = 0
#         deS = 0
#         tupla = map(int,tupl[0].split(","))
#         print("hola",tupla)
#         for i in tupla:
#             idc = i
#             print ("aaa",idc)
#             c.execute("INSERT INTO LineaReparto(idCliente,idReparto,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda) VALUES (?,?,?,?,?,?,?,?,?,?)",(int(idc),idrep[0],co12,co20,coms,pag,fia,de12,de20,deS,))
#             con.commit()
#             idc = 0
#     con.close()

def altaReparto():
    with sqlite3.connect("sifono_db.db") as con:       
        idr = request.form.get('idRepartidor')
        dia = request.form.get('dia')
        idz = request.form.get('zona')
        hab = 1
        c = con.cursor()        
        c.execute("INSERT INTO Reparto(idRepartidor,dia,habilitadoReparto,idZona) VALUES (?,?,?,?)",(idr,dia,hab,idz,))
        con.commit()
    con.close()

def altaLineaReparto():
    with sqlite3.connect("sifono_db.db") as con:
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
        c = con.cursor()
        c.execute("INSERT INTO LineaReparto(idCliente,idReparto,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda) VALUES (?,?,?,?,?,?,?,?,?,?)",(idc,idr,co12,co20,coms,pag,fia,de12,de20,deS,))
        con.commit()
    con.close()

def altaZona():
    with sqlite3.connect("sifono_db.db") as con:
        desc = request.form.get('descripcionZona')       
        c = con.cursor()        
        c.execute("INSERT INTO Zona(descripcion) VALUES (?)",(desc.capitalize(),))
        con.commit()
    con.close()

def altaHistorico():
    with sqlite3.connect("sifono_db.db") as con:
        idr = request.form.get('repartidor')   
        fech = request.form.get('fecha') 
        zona = request.form.get('zona')
        dia = request.form.get('dia')
        c = con.cursor()        
        c.execute("INSERT INTO Historico(repartidor,fecha,zona,dia) VALUES (?,?,?,?)",(idr,fech,zona,dia,))
        con.commit()
    con.close()

def altaHistoricoLinea():
    with sqlite3.connect("sifono_db.db") as con:
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
        c = con.cursor()        
        c.execute("INSERT INTO HistoricoLinea(idHistorico,cliente,domicilio,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,observacion) VALUES (?,?,?,?,?,?,?,]?,?,?,?,?)",(idh,cli,domicilio,com12,com20,comSoda,pago,fiado,dev12,dev20,devSoda,observacion,))
        con.commit()
    con.close()

def habCliente():
    with sqlite3.connect("sifono_db.db") as con:
        idCliente2 = request.form.get('idCliente')       
        c = con.cursor() 
        hab = 1      
        c.execute("UPDATE Cliente SET habilitadoC=? WHERE idCliente = ?", (hab,idCliente2,) )
        con.commit()
    con.close()

def habReparto():
    with sqlite3.connect("sifono_db.db") as con:
        idReparto2 = request.form.get('idReparto')       
        c = con.cursor()        
        hab = 1      
        c.execute("UPDATE Reparto SET habilitadoReparto=? WHERE idReparto = ?", (hab,idReparto2,) )
        # c.execute("DELETE FROM LineaReparto Where idReparto = ?", (idReparto2,))
        con.commit()
    con.close()

def habRepartidor():
    with sqlite3.connect("sifono_db.db") as con:
        idRepartidor2 = request.form.get('idRepartidor')       
        c = con.cursor()        
        hab = 1     
        c.execute("UPDATE Repartidor SET habilitadoRep=? WHERE idRepartidor = ?", (hab,idRepartidor2,))
        con.commit()
    con.close()