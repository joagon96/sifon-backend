from src.executeQuerys import getQueryScalar, getQueryData, getRowData


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

def VentasXmes():
    data = getQueryData("""SELECT strftime('%Y', h.fecha) AS year, strftime('%m', h.fecha) AS month, SUM(hl.pago) AS recaudado
                            FROM Historico h
                            INNER JOIN HistoricoLinea hl on h.idHistorico = hl.idHistorico
                            WHERE h.fecha BETWEEN date('now', '-12 months') AND date('now')
                            GROUP BY strftime('%Y', h.fecha), strftime('%m', h.fecha)
                            ORDER BY strftime('%Y', h.fecha), strftime('%m', h.fecha) DESC;""")
    report = {}
    for month in data:
        monthNumber = int(month['month'])
        report[monthsDict()[monthNumber]] = month['recaudado']
    return report

def ProductosXmes():
    data = getQueryData("""SELECT strftime('%Y', h.fecha) AS year, strftime('%m', h.fecha) AS month, SUM(hl.com12) as 'Bidon 12L', SUM(hl.com20) as 'Bidon 20L', SUM(hl.comSoda) AS 'Sifon Soda'
                            FROM Historico h
                            INNER JOIN HistoricoLinea hl on h.idHistorico = hl.idHistorico
                            WHERE h.fecha BETWEEN date('now', '-12 months') AND date('now')
                            GROUP BY strftime('%Y', h.fecha), strftime('%m', h.fecha)
                            ORDER BY strftime('%Y', h.fecha), strftime('%m', h.fecha) DESC""")
    report = {}
    for month in data:
        monthNumber = int(month['month'])
        producto = {"Bidon 12L": month['Bidon 12L'],"Bidon 20L": month['Bidon 20L'],"Sifon Soda": month['Sifon Soda']}
        report[monthsDict()[monthNumber]] = producto
    return report

def TopProductos():
    data = getRowData("SELECT SUM(com12) as 'Bidon 12L', SUM(com20) as 'Bidon 20L', SUM(comSoda) as 'Sifon Soda' FROM HistoricoLinea;")
    return dict(sorted(data.items(), key=lambda x: x[1],reverse= True))

def ClientesXzona():
    data =  getQueryData("""SELECT descripcion, COUNT(idCliente) as clientes
                            FROM Cliente c
                            INNER JOIN Zona z ON c.idZona = z.idZona
                            WHERE c.habilitadoC = 1 AND z.habilitado = 1
                            GROUP BY z.idZona;""")
    report = {}
    for zona in data:
        report[zona['descripcion']] = zona['clientes']
    return report

def TopClientes():
    data = getQueryData("""SELECT cliente, SUM(pago) pagado
                            FROM HistoricoLinea
                            GROUP BY (cliente)
                            ORDER BY sum(pago) DESC LIMIT 10;""")
    report = {}
    for cliente in data:
        report[cliente['cliente']] = cliente['pagado']
    return report

def TopDeudores():
    data = getQueryData("SELECT nomapeCli, deuda FROM Cliente WHERE habilitadoC = 1 ORDER BY deuda DESC LIMIT 10;")
    report = {}
    for cliente in data:
        report[cliente['nomapeCli']] = cliente['deuda']
    return report

def RepartosXdia():
    data = getQueryData("SELECT dia, COUNT(idReparto) as repartos FROM Reparto WHERE habilitadoReparto = 1 GROUP BY dia ORDER BY COUNT(idReparto) desc")
    report = {}
    for dia in data:
        report[dia['dia']] = dia['repartos']
    return report

def RepartosXzona():
    data = getQueryData("""SELECT descripcion, COUNT(idReparto) as repartos
                            FROM Zona z
                            INNER JOIN Reparto r ON r.idZona = z.idZona
                            WHERE z.habilitado = 1 AND r.habilitadoReparto = 1
                            GROUP BY z.idZona;""")
    report = {}
    for zona in data:
        report[zona['descripcion']] = zona['repartos']
    return report
        
def monthsDict():
    return {1:'ene',2:'feb',3:'mar',4:'abr',5:'may',6:'jun',7:'jul',8:'ago',9:'sep',10:'oct',11:'nov',12:'dic'}
