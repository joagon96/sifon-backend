from flask import Blueprint, render_template, abort
import sqlite3
#conn = sqlite3.connect('sifono_database.db', check_same_thread=False)

querysView = Blueprint('querysView', __name__, template_folder='templates')

#@querysView.route('/execute/<string>')
def executeQuery(string):
    with sqlite3.connect("sifono_db.db") as con:
        c = con.cursor()
        c.execute(string)
        con.commit()
    con.close() 
    return "OK"

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