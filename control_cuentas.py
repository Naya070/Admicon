from glob import glob
from main import *
from tkinter import *
from interfaz_poo import *
from tkinter import ttk
from PIL import ImageTk, Image
from controladorbd import *


class control_cuentas(Frame):

    # CONSTRUCTOR
    def __init__(self, master=None):
        super().__init__(master, width=1440, height=900)
        self.master = master
        self.pack()
        self.create_widgets()

    # WINDOWS
    # Control de cuentas
    def open_control_cuentas(self):
        self = Toplevel()  # la nueva ventana
        self.title("Admicon - Control de Cuentas")
        self.geometry("1440x900")
        self.config(bg="lightblue")

        self.button_recibo = Button(self, text="Recibos", width=20,
                            height=1).place(x=0, y=0)

        self.button_propietarios = Button(
            self, text="Datos Propietarios", width=20, height=1).place(x=420, y=0)
        self.button_correos = Button(self, text="Envío Correos",
                                width=20, height=1).place(x=630, y=0)
        self.button_nomina = Button(self, text="Nómina", width=20,
                            height=1).place(x=840, y=0)

        #registrar_pago =  Button(self, text="Registrar Pago", command= registro_pago, width=20, height=1).place(x = 630, y = 60)
        #añadir_cobro =  Button(self, text="Registrar Cobro", command= añade_cobro, width=20, height=1).place(x = 630, y = 110)

        self.label_button_cuentas = Label(self, text="Control de Cuentas", font=(
            "Arial"), bg="lightblue", width=20, height=1).place(x=210, y=0)
        self.total_pago = Label(self, text="Total Pago:", font=(
            "Arial"), bg="lightblue", width=20, height=1).place(x=20, y=60)
        self.total_pago_mostrar = Label(self, text="12345678,90 Bs", font=(
            "Arial"), bg="lightblue", relief=SUNKEN).place(x=180, y=60, width=150)
        self.porcentaje_mora = Label(self, text="1 % Mora:", font=(
            "Arial"), bg="lightblue", width=20, height=1).place(x=20, y=90)
        self.porcentaje_mora_mostrar = Label(self, text="12345678,90 Bs", font=(
            "Arial"), bg="lightblue", relief=SUNKEN).place(x=180, y=90, width=150)
        self.fecha_self = Label(self, text="Fecha:", font=("Arial"),
                        bg="lightblue", width=20, height=1).place(x=20, y=120)
        self.fecha_self_mostrar = Label(self, text="Día/Mes/Año", font=("Arial"),
                                bg="lightblue", relief=SUNKEN).place(x=180, y=120, width=120)

        # Frame del treeview
        self.frame_3 = Frame(self)
        self.frame_3.pack(fill=BOTH, side=BOTTOM)
        self.frame_3.config(bg="white", width=2440, height=300)

        self.grid = ttk.Treeview(self.frame_3)

        self.treexscroll = Scrollbar(self.frame_3, orient=HORIZONTAL)
        self.treexscroll.pack(fill=X, side=BOTTOM)
        # configurar scrollbar
        self.treexscroll.config(command=self.grid.xview)

        self.treeyscroll = Scrollbar(self.frame_3, orient=VERTICAL)
        self.treeyscroll.pack(fill=Y, side=RIGHT)
        # configurar scrollbar
        self.treeyscroll.config(command=self.grid.yview)

        # TREEVIEW
        self.grid.config(xscrollcommand=self.treexscroll.set, yscrollcommand=self.treeyscroll.set,
        columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10"))

        self.grid.column("#0", width= 50, stretch= False)
        self.grid.column("col1", width=150, stretch= False)
        self.grid.column("col2", width=150, stretch= False)
        self.grid.column("col3", width=150, stretch= False)
        self.grid.column("col4", width=160, stretch= False)
        self.grid.column("col5", width=150, stretch= False)
        self.grid.column("col6", width=150, stretch= False)
        self.grid.column("col7", width=150, stretch= False)
        self.grid.column("col8", width=150, stretch= False)
        self.grid.column("col9", width=150, stretch= False)
        self.grid.column("col10", width=150, stretch= False)

        self.grid.heading("#0", text="ID", anchor=CENTER)
        self.grid.heading("col1", text="Deudas del mes pasado", anchor=CENTER)
        self.grid.heading("col2", text="Recibo monto", anchor=CENTER)
        self.grid.heading("col3", text="Mora", anchor=CENTER)
        self.grid.heading("col4", text="Alquiler estacionamiento", anchor=CENTER)
        self.grid.heading("col5", text="Deuda actual", anchor=CENTER)
        self.grid.heading("col6", text="Bolívares", anchor=CENTER)
        self.grid.heading("col7", text="Dólares", anchor=CENTER)
        self.grid.heading("col8", text="Fecha", anchor=CENTER)
        self.grid.heading("col9", text="Cambio del día", anchor=CENTER)
        self.grid.heading("col10", text="Saldo", anchor=CENTER)

        self.grid.pack(fill = BOTH, side=BOTTOM, expand= True)
