from src.executeQuerys import getQueryScalar, getQuerySum

def ContadorClientes():
    hab = 1
    return getQueryScalar("SELECT COUNT(*) FROM Cliente WHERE habilitadoC=?",(hab,))

def ContadorZonas():
    hab = 1       
    return getQueryScalar("SELECT COUNT(*) FROM Zona WHERE habilitado=?",(hab,))

def ContadorRepartidores():
    hab = 1     
    return getQueryScalar("SELECT COUNT(*) FROM Repartidor WHERE habilitadoRep=?", (hab,))

def ContadorRepartos():
    hab = 1      
    return getQueryScalar("SELECT COUNT(*) FROM Reparto WHERE habilitadoReparto=?", (hab,))

def ContadorBidones12():   
    return getQuerySum("SELECT com12 FROM Reparto")

def ContadorBidones20():
    return getQuerySum("SELECT com20 FROM Reparto")

def ContadorSoda():
    return getQuerySum("SELECT comSoda FROM Reparto")
