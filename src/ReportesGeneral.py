import sqlite3

def ContadorClientes():
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute("SELECT COUNT(*) FROM Cliente")
            cantidad=c.fetchone()
            return cantidad
    con.close()

def ContadorZonas():
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute("SELECT COUNT(*) FROM Zona")
            cantidad=c.fetchone()
            return cantidad
    con.close()

def ContadorRepartidores():
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute("SELECT COUNT(*) FROM Repartidor")
            cantidad=c.fetchone()
            return cantidad
    con.close()


def ContadorRepartos():
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute("SELECT COUNT(*) FROM Reparto")
            cantidad=c.fetchone()
            return cantidad
    con.close()

def ContadorBidones12():
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute("SELECT com12 FROM Reparto")
            cantidad=c.fetchall()
            suma=0
            for i in cantidad:
                for j in i:
                    suma = suma + j 
            return suma
    con.close()

def ContadorBidones20():
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute("SELECT com20 FROM Reparto")
            cantidad=c.fetchall()
            suma=0
            for i in cantidad:
                for j in i:
                    suma = suma + j 
            return suma
    con.close()

def ContadorSoda():
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute("SELECT comSoda FROM Reparto")
            cantidad=c.fetchall()
            suma=0
            for i in cantidad:
                for j in i:
                    suma = suma + j 
            return suma
    con.close()