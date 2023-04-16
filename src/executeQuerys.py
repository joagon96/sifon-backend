from flask import Blueprint, render_template, abort
import sqlite3

querysView = Blueprint('querysView', __name__, template_folder='templates')

def executeQuery(string):
    with sqlite3.connect("sifono_db.db") as con:
        c = con.cursor()
        c.execute(string)
        con.commit()
    con.close() 
    return "OK"

def getQueryData(string):
    queryData = []
    with sqlite3.connect("sifono_db.db") as con:
        c = con.cursor()
        c.execute(string)
        rows = c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        for rowsValues in rows:
            dictA = {}
            for i, value in enumerate(rowsValues):
                dictA[names[i]] = value
            queryData.append(dictA)

    return queryData

def getQueryScalar(string):
    with sqlite3.connect("sifono_db.db") as con:
            c = con.cursor()        
            c.execute(string)
            scalar=c.fetchone()
            return scalar
    con.close()

#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
#conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()