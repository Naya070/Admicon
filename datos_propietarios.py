from main import *
from tkinter import *
from interfaz_poo import *
from tkinter import ttk
from PIL import ImageTk, Image
from controladorbd import *

class datos_propietarios(Frame):

    # CONSTRUCTOR
    def __init__(self, master=None):
        super().__init__(master, width=1440, height=900)
        self.master = master
        self.pack()
        self.create_widgets()

    def datos_propietarios(self):
        self = Toplevel() #la nueva ventana
        self.title("Admicon - Datos de Propietarios")
        self.geometry("1440x900")
        self.config(bg="lightblue")

        self.frame_4 = Frame(self)
        self.frame_4.place(x = 0, y = 260)
        self.frame_4.config(bg="white", width=1440, height=300)

        #Buttons
        self.button_recibo = Button(self, text="Recibos", width=20, height=1 ).place(x = 0, y = 0)      
        self.button_cuentas = Button(self, text="Control de Cuentas", width=20, height=1).place(x = 210, y = 0)     
        
        self.button_correos = Button(self, text="Envío Correos", width=20, height=1).place(x = 630, y = 0) 
        self.button_nomina = Button(self, text="Nómina", width=20, height=1).place(x = 840, y = 0)  

        self.actualizar = Button(self, text="Actualizar", width=20, height=1).place(x = 840, y = 180)  


        #Labels
        self.label_button_propietarios = Label(self, text="Datos Propietarios", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 420, y = 0) 

        self.buscar= Label(self, text="Buscar:", font=("Arial"), bg="lightblue" ).place(x=10, y=40)  
        self.modificar_datos= Label(self, text="Modificar Datos", font=("Arial"), bg="lightblue" ).place(x=10, y=100)  
        self.propietario= Label(self, text="Propietario", font=("Arial"), bg="lightblue" ).place(x=400, y=100) 
        self.apartamento = Label(self, text="Apartamento:", font=("Arial"), bg="lightblue" ).place(x=10, y=150)  
        self.nombre_apellido = Label(self, text="Nombre y Apellido:", font=("Arial"), bg="lightblue" ).place(x=450, y=150)
        self.telefono = Label(self, text="Teléfono:", font=("Arial"), bg="lightblue" ).place(x=450, y=180)
        self.correo = Label(self, text="Correo:", font=("Arial"), bg="lightblue" ).place(x=450, y=210)


        #Entry
        self.buscar = Entry(self).place(x=150, y=43, width=200)
        self.apartamento_entry = Entry(self).place(x=150, y=150, width=200)
        self.nombre_apellido_entry= Entry(self).place(x=600, y=150, width=200)
        self.telefono_entry = Entry(self).place(x=600, y=180, width=200)
        self.correo_entry = Entry(self).place(x=600, y=210, width=200)
