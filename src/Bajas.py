from flask import request
from src.executeQuerys import executeQuery, getQueryData

def bajaCliente():
    idCliente2 = request.form.get('idCliente')       
    hab = 0      
    executeQuery("UPDATE Cliente SET habilitadoC=? WHERE idCliente = ?", (hab,idCliente2,) )

def bajaRepartidor():
    idRepartidor2 = request.form.get('idRepartidor')
    data = getQueryData("SELECT nomapeRep FROM Repartidor WHERE idRepartidor = ?", (idRepartidor2,))     
    hab = 0      
    executeQuery("UPDATE Repartidor SET habilitadoRep=? WHERE idRepartidor = ?", (hab,idRepartidor2,))
    executeQuery("DELETE FROM Usuario WHERE usuario=?", (data[0]['nomapeRep'],))

def bajaReparto():
    idReparto2 = request.form.get('idReparto')            
    hab = 0      
    executeQuery("UPDATE Reparto SET habilitadoReparto=? WHERE idReparto = ?", (hab,idReparto2,) )

def bajaLineaReparto():
    idlr = request.form.get('idLineaReparto')             
    executeQuery("DELETE FROM LineaReparto WHERE idLR = ?", (idlr,) )