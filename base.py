from optparse import Values
import sqlite3
from gui import *


class Controlador:

    def __init__(self):
        self.my_connexion = sqlite3.connect("Admicon.db")

    try:
        my_connexion = sqlite3.connect("Admicon.db")
        cursor = my_connexion.cursor()
        cursor.execute("SELECT * FROM Datos_por_apartamento")
        rows = cursor.fetchall()
        #for row in rows:
        #    print(row)

    except Exception as ex:
        print(ex)


    def consulta_cuentas(self):
        self.my_connexion = sqlite3.connect("Admicon.db")
        cursor = self.my_connexion.cursor()
        cursor.execute("SELECT * FROM Cuentas_por_apartamento")
        datos = cursor.fetchall()
        cursor.close()
        self.my_connexion.close()
        return datos

    def consulta_total(self):
        self.my_connexion = sqlite3.connect("Admicon.db")
        cursor = self.my_connexion.cursor()
        cursor.execute("SELECT * FROM Total_apto")
        datos = cursor.fetchall()
        cursor.close()
        self.my_connexion.close()
        return datos

    def consulta_datos_apto(self):
        self.my_connexion = sqlite3.connect("Admicon.db")
        cursor = self.my_connexion.cursor()
        cursor.execute("SELECT * FROM Datos_por_apartamento")
        datos = cursor.fetchall()
        cursor.close()
        self.my_connexion.close()
        return datos

    def consulta_datos_recibo(self):
        self.my_connexion = sqlite3.connect("Admicon.db")
        cursor = self.my_connexion.cursor()
        cursor.execute("SELECT * FROM Recibo")
        datos = cursor.fetchall()
        cursor.close()
        self.my_connexion.close()
        return datos

    def __str__(self):
        datos = self.consulta_cuentas()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux 
 

    def inserta_cuentas(self,Deudas_mes_pasado, Recibo, Mora, Aquiler_estacionamiento,
        Deuda_actual, Pago_Bs, Pago_USD, Fecha, Cambio, Saldo):
        cursor = self.my_connexion.cursor()
        sql = '''INSERT INTO Cuentas_por_apartamento (Deudas_mes_pasado, Recibo, 
        Mora, Aquiler_estacionamiento, Deuda_actual, Pago_Bs, Pago_USD, Fecha, Cambio, Saldo)
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}',  '{}', '{}',
        '{}', '{}' ) '''.format( Deudas_mes_pasado, Recibo, Mora, Aquiler_estacionamiento,
        Deuda_actual, Pago_Bs, Pago_USD, Fecha, Cambio, Saldo)
        cursor.execute(sql)
        n = cursor.rowcount
        self.my_connexion.commit()
        cursor.close()
        return n


    def mostrar(self):
        self.my_connexion = sqlite3.connect("Admicon.db")
        cursor = self.my_connexion.cursor()
        con_cuentas =Control_cuentas()
        registros = con_cuentas.self.tree.get_children()
        for elemento in registros:
            con_cuentas.tree.delete(elemento)

        try:
            cursor.execute("SELECT * FROM Datos_por_apartamento")
            for row in cursor:
                con_cuentas.tree.insert("",0, text= row[0], values =(row[1], row[2], row[3],
                row[4], row[5], row[6], row[7],row[8], row[9], row[10], row[11], 
                row[12], row[13]))

        except:
            pass


    def borrar_cuentas(self):
        pass
