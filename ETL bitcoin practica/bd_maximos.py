import sqlite3 as bd

def creacion():
    con=bd.connect('Maximos_Bitcoin.db')
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Maximos(
                    fecha FECHA,
                    Maximo FLOAT
        )''')
    cur.close()
    con.close()


def cargar_datos(fecha,maximo):
    creacion()
    con=bd.connect('Maximos_Bitcoin.db')
    cur=con.cursor()
    for fechas,maximos in zip(fecha,maximo):
            cur.execute('INSERT INTO Maximos (fecha,maximo) VALUES (?,?)',(fechas,maximos))
    con.commit()
    cur.close()
    con.close()
    
def borrar_datos():
    con=bd.connect('Maximos_Bitcoin.db')
    cur=con.cursor()
    cur.execute('DROP TABLE Maximos')
    con.commit()
    cur.close()
    con.close()
        
def mostrar_datos():
    con=bd.connect('Maximos_Bitcoin.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM Maximos ORDER BY fecha')
    datos=cur.fetchall()
    for x in datos:
        print(x)
    cur.close()
    con.close()