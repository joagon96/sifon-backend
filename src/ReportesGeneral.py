from src.executeQuerys import getQueryScalar, getQuerySum


def ContadorClientes():
    hab = 1
    return getQueryScalar("SELECT COUNT(*) FROM Cliente WHERE habilitadoC=?", (hab,))


def ContadorZonas():
    hab = 1
    return getQueryScalar("SELECT COUNT(*) FROM Zona WHERE habilitado=?", (hab,))


def ContadorRepartidores():
    hab = 1
    return getQueryScalar("SELECT COUNT(*) FROM Repartidor WHERE habilitadoRep=?", (hab,))


def ContadorRepartos():
    hab = 1
    return getQueryScalar("SELECT COUNT(*) FROM Reparto WHERE habilitadoReparto=?", (hab,))


def ContadorHistoricos():
    return getQueryScalar("SELECT COUNT(*) FROM Historico")


def ContadorBidones12():
    return getQueryScalar("SELECT SUM(com12) FROM HistoricoLinea")


def ContadorBidones20():
    return getQueryScalar("SELECT SUM(com20) FROM HistoricoLinea")


def ContadorSoda():
    return getQueryScalar("SELECT SUM(comSoda) FROM HistoricoLinea")


def ContadorPagos():
    return getQueryScalar("SELECT SUM(pago) FROM HistoricoLinea")


def ContadorFiados():
    return getQueryScalar("SELECT SUM(fiado) FROM HistoricoLinea")
