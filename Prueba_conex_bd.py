import sqlite3

try:
    my_connexion = sqlite3.connect("Admicon.db")
    cursor = my_connexion.cursor()
    cursor.execute("SELECT * FROM Datos_por_apartamento")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print(ex)