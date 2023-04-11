from flask import Flask, render_template, jsonify, request
import json
from src.executeQuerys import querysView
from src.executeQuerys import executeQuery
import sqlite3

def bajaCliente():
    with sqlite3.connect("sifono_db.db") as con:
        idCliente2 = request.form.get('idCliente')       
        c = con.cursor() 
        hab = 0      
        c.execute("UPDATE Cliente SET habilitadoC=? WHERE idCliente = ?", (hab,idCliente2,) )
        con.commit()
    con.close()

def bajaRepartidor():
    with sqlite3.connect("sifono_db.db") as con:
        idRepartidor2 = request.form.get('idRepartidor')       
        c = con.cursor()        
        hab = 0      
        c.execute("UPDATE Repartidor SET habilitadoRep=? WHERE idRepartidor = ?", (hab,idRepartidor2,))
        con.commit()
    con.close()

def bajaReparto():
    with sqlite3.connect("sifono_db.db") as con:
        idReparto2 = request.form.get('idReparto')       
        c = con.cursor()        
        hab = 0      
        c.execute("UPDATE Reparto SET habilitadoReparto=? WHERE idReparto = ?", (hab,idReparto2,) )
        # c.execute("DELETE FROM LineaReparto Where idReparto = ?", (idReparto2,))
        con.commit()
    con.close()

# def bajaZona():
#     with sqlite3.connect("sifono_db.db") as con:
#         idZona2 = request.form.get('idZona')       
#         c = con.cursor()        
#         c.execute("DELETE FROM Zona WHERE idZona = ?", (idZona2,) )
#         con.commit()
#     con.close()

def bajaLineaReparto():
    with sqlite3.connect("sifono_db.db") as con:
        idlr = request.form.get('idLineaReparto')       
        c = con.cursor()        
        c.execute("DELETE FROM LineaReparto WHERE idLR = ?", (idlr,) )
        con.commit()
    con.close()