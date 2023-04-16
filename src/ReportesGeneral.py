from src.executeQuerys import getQueryScalar, getQuerySum

def ContadorClientes():
    return getQueryScalar("SELECT COUNT(*) FROM Cliente")

def ContadorZonas():       
    return getQueryScalar("SELECT COUNT(*) FROM Zona")

def ContadorRepartidores():     
    return getQueryScalar("SELECT COUNT(*) FROM Repartidor")

def ContadorRepartos():      
    return getQueryScalar("SELECT COUNT(*) FROM Reparto")

def ContadorBidones12():   
    return getQuerySum("SELECT com12 FROM Reparto")

def ContadorBidones20():
    return getQuerySum("SELECT com20 FROM Reparto")

def ContadorSoda():
    return getQuerySum("SELECT comSoda FROM Reparto")
