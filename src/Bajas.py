from flask import request
from src.executeQuerys import executeQuery

def bajaCliente():
    idCliente2 = request.form.get('idCliente')       
    hab = 0      
    executeQuery("UPDATE Cliente SET habilitadoC=? WHERE idCliente = ?", (hab,idCliente2,) )

def bajaRepartidor():
    idRepartidor2 = request.form.get('idRepartidor')            
    hab = 0      
    executeQuery("UPDATE Repartidor SET habilitadoRep=? WHERE idRepartidor = ?", (hab,idRepartidor2,))

def bajaReparto():
    idReparto2 = request.form.get('idReparto')            
    hab = 0      
    executeQuery("UPDATE Reparto SET habilitadoReparto=? WHERE idReparto = ?", (hab,idReparto2,) )

def bajaLineaReparto():
    idlr = request.form.get('idLineaReparto')             
    executeQuery("DELETE FROM LineaReparto WHERE idLR = ?", (idlr,) )