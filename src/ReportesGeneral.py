import sqlite3
from src.executeQuerys import getQueryScalar

def ContadorClientes():
    return getQueryScalar("SELECT COUNT(*) FROM Cliente")

def ContadorZonas():       
    return getQueryScalar("SELECT COUNT(*) FROM Zona")

def ContadorRepartidores():     
    return getQueryScalar("SELECT COUNT(*) FROM Repartidor")

def ContadorRepartos():      
    return getQueryScalar("SELECT COUNT(*) FROM Reparto")

def ContadorBidones12():   
    return calcularSumatoria("SELECT com12 FROM Reparto")

def ContadorBidones20():
    return calcularSumatoria("SELECT com20 FROM Reparto")

def ContadorSoda():
    return calcularSumatoria("SELECT comSoda FROM Reparto")

def calcularSumatoria(query):
     with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute(query)
            cantidad=c.fetchall()
            suma=0
            for i in cantidad:
                for j in i:
                    suma = suma + j 
            return suma
            con.close()
