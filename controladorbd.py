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


def consulta_cuentas():
    cursor = my_connexion.cursor()
    cursor.execute("SELECT * FROM Datos_por_apartamento")
    datos = cursor.fetchall()
    cursor.close()
    my_connexion.close()
    return datos

def __str__():
    datos = consulta_cuentas()
    aux = ""
    for row in datos:
        aux = aux + str(row) + "\n"
    return aux


def inserta_cuentas(Deudas_mes_pasado, Recibo, Mora, Aquiler_estacionamiento,
      Deuda_actual, Pago_Bs, Pago_USD, Fecha, Cambio, Saldo):
    cursor = my_connexion.cursor()
    sql = '''INSERT INTO Cuentas_por_apartamento (Deudas_mes_pasado, Recibo, 
    Mora, Aquiler_estacionamiento, Deuda_actual, Pago_Bs, Pago_USD, Fecha, Cambio, Saldo)
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}',  '{}', '{}',
     '{}', '{}' ) '''.format( Deudas_mes_pasado, Recibo, Mora, Aquiler_estacionamiento,
      Deuda_actual, Pago_Bs, Pago_USD, Fecha, Cambio, Saldo)
    cursor.execute(sql)
    n = cursor.rowcount
    my_connexion.commit()
    cursor.close()
    return n 

def borrar_cuentas():
    pass