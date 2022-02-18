from glob import glob
from main import *
from tkinter import *
from interfaz_poo import *
from tkinter import ttk
from PIL import ImageTk, Image


# WINDOWS
# Control de cuentas
def open_control_cuentas():
    occ = Toplevel()  # la nueva ventana
    occ.title("Admicon - Control de Cuentas")
    occ.geometry("1440x900")
    occ.config(bg="lightblue")

    button_recibo = Button(occ, text="Recibos", width=20,
                           height=1).place(x=0, y=0)

    button_propietarios = Button(
        occ, text="Datos Propietarios", width=20, height=1).place(x=420, y=0)
    button_correos = Button(occ, text="Envío Correos",
                            width=20, height=1).place(x=630, y=0)
    button_nomina = Button(occ, text="Nómina", width=20,
                           height=1).place(x=840, y=0)

    #registrar_pago =  Button(occ, text="Registrar Pago", command= registro_pago, width=20, height=1).place(x = 630, y = 60)
    #añadir_cobro =  Button(occ, text="Registrar Cobro", command= añade_cobro, width=20, height=1).place(x = 630, y = 110)

    label_button_cuentas = Label(occ, text="Control de Cuentas", font=(
        "Arial"), bg="lightblue", width=20, height=1).place(x=210, y=0)
    total_pago = Label(occ, text="Total Pago:", font=(
        "Arial"), bg="lightblue", width=20, height=1).place(x=20, y=60)
    total_pago_mostrar = Label(occ, text="12345678,90 Bs", font=(
        "Arial"), bg="lightblue", relief=SUNKEN).place(x=180, y=60, width=150)
    porcentaje_mora = Label(occ, text="1 % Mora:", font=(
        "Arial"), bg="lightblue", width=20, height=1).place(x=20, y=90)
    porcentaje_mora_mostrar = Label(occ, text="12345678,90 Bs", font=(
        "Arial"), bg="lightblue", relief=SUNKEN).place(x=180, y=90, width=150)
    fecha_occ = Label(occ, text="Fecha:", font=("Arial"),
                      bg="lightblue", width=20, height=1).place(x=20, y=120)
    fecha_occ_mostrar = Label(occ, text="Día/Mes/Año", font=("Arial"),
                              bg="lightblue", relief=SUNKEN).place(x=180, y=120, width=120)

    # Frame del treeview
    frame_3 = Frame(occ)
    frame_3.pack(fill=BOTH, side=BOTTOM)
    frame_3.config(bg="white", width=2440, height=300)

    grid = ttk.Treeview(frame_3)

    treexscroll = Scrollbar(frame_3, orient=HORIZONTAL)
    treexscroll.pack(fill=X, side=BOTTOM)
    # configurar scrollbar
    treexscroll.config(command=grid.xview)

    treeyscroll = Scrollbar(frame_3, orient=VERTICAL)
    treeyscroll.pack(fill=Y, side=RIGHT)
    # configurar scrollbar
    treeyscroll.config(command=grid.yview)

    # TREEVIEW
    grid.config(xscrollcommand=treexscroll.set, yscrollcommand=treeyscroll.set,
       columns=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10"))

    grid.column("#0", width= 50, stretch= False)
    grid.column("col1", width=150, stretch= False)
    grid.column("col2", width=150, stretch= False)
    grid.column("col3", width=150, stretch= False)
    grid.column("col4", width=160, stretch= False)
    grid.column("col5", width=150, stretch= False)
    grid.column("col6", width=150, stretch= False)
    grid.column("col7", width=150, stretch= False)
    grid.column("col8", width=150, stretch= False)
    grid.column("col9", width=150, stretch= False)
    grid.column("col10", width=150, stretch= False)

    grid.heading("#0", text="ID", anchor=CENTER)
    grid.heading("col1", text="Deudas del mes pasado", anchor=CENTER)
    grid.heading("col2", text="Recibo monto", anchor=CENTER)
    grid.heading("col3", text="Mora", anchor=CENTER)
    grid.heading("col4", text="Alquiler estacionamiento", anchor=CENTER)
    grid.heading("col5", text="Deuda actual", anchor=CENTER)
    grid.heading("col6", text="Bolívares", anchor=CENTER)
    grid.heading("col7", text="Dólares", anchor=CENTER)
    grid.heading("col8", text="Fecha", anchor=CENTER)
    grid.heading("col9", text="Cambio del día", anchor=CENTER)
    grid.heading("col10", text="Saldo", anchor=CENTER)

    grid.pack(fill = BOTH, side=BOTTOM, expand= True)
