from glob import glob
from tkinter import *

class Ventana(Frame):
    '''
        abre una ventana

        frame:dato tipo frame
    '''
    def __init__(self, master=None):
        super().__init__(master, width=1440, height=900)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass   



root = Tk()
root.title("Admicon - Recibo")
root.geometry("1440x900")
root.config(bg="lightblue")

frame_3 = Frame(root) #Frame de visualizacion de recibo
frame_3.place(x = 500, y = 30)
frame_3.config(bg="white", width=700, height=400)


    

#WINDOWS
#Control de cuentas
def open_control_cuentas():
    occ = Toplevel() #la nueva ventana
    occ.title("Admicon - Control de Cuentas")
    occ.geometry("1440x900")
    occ.config(bg="lightblue")

    frame_3 = Frame(occ)
    frame_3.place(x = 0, y = 260)
    frame_3.config(bg="white", width=1440, height=300)

    button_recibo = Button(occ, text="Recibos", width=20, height=1 ).place(x = 0, y = 0)                            
    
    button_propietarios = Button(occ, text="Datos Propietarios", width=20, height=1).place(x = 420, y = 0) 
    button_correos = Button(occ, text="Envío Correos", width=20, height=1).place(x = 630, y = 0)  
    button_nomina = Button(occ, text="Nómina", width=20, height=1).place(x = 840, y = 0)  

    registrar_pago =  Button(occ, text="Registrar Pago", command= registro_pago, width=20, height=1).place(x = 630, y = 60)
    añadir_cobro =  Button(occ, text="Registrar Cobro", command= añade_cobro, width=20, height=1).place(x = 630, y = 110)



    label_button_cuentas = Label(occ, text="Control de Cuentas", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 210, y = 0)
    total_pago = Label(occ, text="Total Pago:", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 20, y = 60) 
    total_pago_mostrar = Label(occ, text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=180, y=60, width=150) 
    porcentaje_mora = Label(occ, text="1 % Mora:", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 20, y = 90)                                   
    porcentaje_mora_mostrar = Label(occ, text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=180, y=90, width=150) 
    fecha_occ = Label(occ, text="Fecha:", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 20, y = 120)                                   
    fecha_occ_mostrar = Label(occ, text="Día/Mes/Año", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=180, y=120, width=120)

def registro_pago():
    rp = Toplevel() #la nueva ventana
    rp.title("Registrar Pago")
    rp.geometry("500x500")
    rp.config(bg="lightblue")  

    registro_de_pago= Label(rp, text="Registro de Pago:", font=("Arial"), bg="lightblue" ).place(x=180, y=10) 
    apartamento= Label(rp, text="Apartamento:", font=("Arial"), bg="lightblue" ).place(x=30, y=80) 
    acumulado= Label(rp, text="Acumulado:", font=("Arial"), bg="lightblue" ).place(x=30, y=130) 
    monto= Label(rp, text="Monto:", font=("Arial"), bg="lightblue" ).place(x=30, y=180) 
    restante= Label(rp, text="Restante:", font=("Arial"), bg="lightblue" ).place(x=30, y=400) 

    apartamento_entry = Entry(rp).place(x=140, y=80, width=200)
    monto_entry = Entry(rp).place(x=140, y=180, width=200)

    acumulado_label = Label(rp, text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=140, y=130, width=200) 
    Monto_Bs = Label(rp, text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=140, y=200, width=200) 
    restante_mostrar = Label(rp, text="0,00 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=140, y=400, width=200) 

    a = IntVar()
    Radiobutton(rp, text="Bs", variable=a, value=1, bg="lightblue" ).place(x=400, y=180)
    Radiobutton(rp, text="$", variable=a, value=2, bg="lightblue" ).place(x=350, y=180)

    acumulado_mostrar =  Button(rp, text="Mostrar Acumulado", width=15, height=1).place(x = 350, y = 80)
    añadir =  Button(rp, text="Añadir", width=15, height=1).place(x = 150, y = 300)


def añade_cobro():
    ac = Toplevel() #la nueva ventana
    ac.title("Añadir Cobro")
    ac.geometry("500x500")
    ac.config(bg="lightblue")  

    añadir_cobro= Label(ac, text="Añadir Cobro:", font=("Arial"), bg="lightblue" ).place(x=180, y=10) 
    apartamento= Label(ac, text="Apartamento:", font=("Arial"), bg="lightblue" ).place(x=30, y=60)  
    acumulado= Label(ac, text="Acumulado:", font=("Arial"), bg="lightblue" ).place(x=30, y=100) 
    monto= Label(ac, text="Monto:", font=("Arial"), bg="lightblue" ).place(x=30, y=200) 
    restante= Label(ac, text="Restante:", font=("Arial"), bg="lightblue" ).place(x=30, y=400) 

    apartamento_entry = Entry(ac).place(x=140, y=60, width=200)
    monto_entry = Entry(ac).place(x=140, y=200, width=200)

    acumulado_label = Label(ac, text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=140, y=100, width=200) 
    Monto_Bs = Label(ac, text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=140, y=220, width=200) 
    restante_mostrar = Label(ac, text="0,00 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=140, y=400, width=200) 

    a = IntVar()
    Radiobutton(ac, text="Bs", variable=a, value=1, bg="lightblue" ).place(x=400, y=200)
    Radiobutton(ac, text="$", variable=a, value=2, bg="lightblue" ).place(x=350, y=200)

    b = IntVar()
    Radiobutton(ac, text="Alq. Estacionamiento", variable=b, value=1, bg="lightblue" ).place(x=350, y=100)
    Radiobutton(ac, text="Cuota Extra", variable=b, value=2, bg="lightblue" ).place(x=350, y=120)

    cba = StringVar() #variable var entero
    c = Checkbutton(ac, text= "Añadir a Todos los Apartamentos", variable= cba, onvalue = "On", offvalue= "Off", font=("Arial"), bg="lightblue")
    c.deselect()
    c.place(x=30, y=150)

    acumulado_mostrar =  Button(ac, text="Mostrar Acumulado",  width=15, height=1).place(x = 350, y = 60)
    añadir =  Button(ac, text="Añadir", width=15, height=1).place(x = 150, y = 300)

def datos_propietarios():
    dp = Toplevel() #la nueva ventana
    dp.title("Admicon - Datos de Propietarios")
    dp.geometry("1440x900")
    dp.config(bg="lightblue")

    frame_4 = Frame(dp)
    frame_4.place(x = 0, y = 260)
    frame_4.config(bg="white", width=1440, height=300)

    #Buttons
    button_recibo = Button(dp, text="Recibos", width=20, height=1 ).place(x = 0, y = 0)      
    button_cuentas = Button(dp, text="Control de Cuentas", command= open_control_cuentas, width=20, height=1).place(x = 210, y = 0)     
    
    button_correos = Button(dp, text="Envío Correos", width=20, height=1).place(x = 630, y = 0) 
    button_nomina = Button(dp, text="Nómina", width=20, height=1).place(x = 840, y = 0)  

    actualizar = Button(dp, text="Actualizar", width=20, height=1).place(x = 840, y = 180)  


    #Labels
    label_button_propietarios = Label(dp, text="Datos Propietarios", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 420, y = 0) 

    buscar= Label(dp, text="Buscar:", font=("Arial"), bg="lightblue" ).place(x=10, y=40)  
    modificar_datos= Label(dp, text="Modificar Datos", font=("Arial"), bg="lightblue" ).place(x=10, y=100)  
    propietario= Label(dp, text="Propietario", font=("Arial"), bg="lightblue" ).place(x=400, y=100) 
    apartamento = Label(dp, text="Apartamento:", font=("Arial"), bg="lightblue" ).place(x=10, y=150)  
    nombre_apellido = Label(dp, text="Nombre y Apellido:", font=("Arial"), bg="lightblue" ).place(x=450, y=150)
    telefono = Label(dp, text="Teléfono:", font=("Arial"), bg="lightblue" ).place(x=450, y=180)
    correo = Label(dp, text="Correo:", font=("Arial"), bg="lightblue" ).place(x=450, y=210)


    #Entry
    buscar = Entry(dp).place(x=150, y=43, width=200)
    apartamento_entry = Entry(dp).place(x=150, y=150, width=200)
    nombre_apellido_entry= Entry(dp).place(x=600, y=150, width=200)
    telefono_entry = Entry(dp).place(x=600, y=180, width=200)
    correo_entry = Entry(dp).place(x=600, y=210, width=200)


def correos_envio():
    ce = Toplevel() #la nueva ventana
    ce.title("Admicon - Envío de Correos")
    ce.geometry("1440x900")
    ce.config(bg="lightblue")

   #Labels
    individual_correo = Label(ce, text="INDIVIDUAL", font=("Arial"), bg="lightblue" ).place(x=10, y=40) 
    apartamento = Label(ce, text="Apartamento:", font=("Arial"), bg="lightblue" ).place(x=10, y=100)  

    global_correo = Label(ce, text="GLOBAL", font=("Arial"), bg="lightblue" ).place(x=500, y=40) 

    label_button_correo = Label(ce, text="Envío Correos", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 630, y = 0) 

    #Entry
    apartamento_entry = Entry(ce).place(x=150, y=98, width=200) 

    #Buttons
    button_recibo = Button(ce, text="Recibos", width=20, height=1 ).place(x = 0, y = 0)      
    button_cuentas = Button(ce, text="Control de Cuentas", command= open_control_cuentas, width=20, height=1).place(x = 210, y = 0)     
    button_propietarios = Button(ce, text="Datos Propietarios", command= datos_propietarios, width=20, height=1).place(x = 420, y = 0) 
    
    button_nomina = Button(ce, text="Nómina", width=20, height=1).place(x = 840, y = 0)  

    #checkbuttons
    cea = StringVar() #variable var entero
    c = Checkbutton(ce, text= "Enviar recibo", variable= cea, onvalue = "On", offvalue= "Off", font=("Arial"), bg="lightblue")
    c.deselect()
    c.place(x=30, y=150)

    ceb = StringVar() #variable var entero
    c = Checkbutton(ce, text= "Añadir Recordatorio de Morosidad", variable= ceb, onvalue = "On", offvalue= "Off", font=("Arial"), bg="lightblue")
    c.deselect()
    c.place(x=30, y=180)

    cec = StringVar() #variable var entero
    c = Checkbutton(ce, text= "Enviar Recibo a Todos los Propietarios", variable= cec, onvalue = "On", offvalue= "Off", font=("Arial"), bg="lightblue")
    c.deselect()
    c.place(x=450, y=180)

    ced = StringVar() #variable var entero
    c = Checkbutton(ce, text= "Enviar Recordatorio de Morosidad a Todos los Morosos", variable= ced, onvalue = "On", offvalue= "Off", font=("Arial"), bg="lightblue")
    c.deselect()
    c.place(x=450, y=280)



#BUTTONS                         
button_cuentas = Button(root, text="Control de Cuentas", command= open_control_cuentas, width=20, height=1).place(x = 210, y = 0)     
button_propietarios = Button(root, text="Datos Propietarios", command= datos_propietarios, width=20, height=1).place(x = 420, y = 0) 
button_correos = Button(root, text="Envío Correos", command = correos_envio, width=20, height=1).place(x = 630, y = 0) 
button_nomina = Button(root, text="Nómina", width=20, height=1).place(x = 840, y = 0)                         
crear =  Button(root, text="Crear", width=4, height=1).place(x = 410, y = 80)

button_añadir =  Button(root, text="Añadir", width=20, height=1).place(x = 210, y = 260)
eliminar =  Button(root, text="Eliminar", width=10, height=1).place(x = 10, y = 380)
guardar =  Button(root, text="Guardar", width=10, height=1).place(x = 210, y = 380)

refrescar =  Button(root, text="R", width=20, height=1).place(x = 510, y = 448, width=30)

aceptar_bcv =  Button(root, text="Aceptar", width=20, height=1).place(x = 550, y = 448, width=50)
aceptar_libre =  Button(root, text="Aceptar", width=20, height=1).place(x = 550, y = 498, width=50)



#Labels
label_button_recibo = Label(root, text="Recibos", font=("Arial"), bg="lightblue", width=20, height=1 ).place(x = 0, y = 0)   

vista_recibo= Label(text="Vista preliminar recibo:", font=("Arial"), bg="lightblue" ).place(x=10, y=40)
nuevo_recibo= Label(text="Nuevo recibo:", font=("Arial"), bg="lightblue" ).place(x=10, y=80)
añadir_item= Label(text="Añadir ítems:", font=("Arial"), bg="lightblue" ).place(x=10, y=120)
seccion= Label(text="Sección:", font=("Arial"), bg="lightblue" ).place(x=10, y=140)
descripcion= Label(text="Descripción:", font=("Arial"), bg="lightblue" ).place(x=10, y=180)
monto= Label(text="Monto:", font=("Arial"), bg="lightblue" ).place(x=10, y=220)
eliminar_item= Label(text="Eliminar ítems:", font=("Arial"), bg="lightblue" ).place(x=10, y=300)


fecha =Label(text="Fecha:", font=("Arial"), bg="lightblue" ).place(x=10, y=450)
fecha_mostrar = Label(text="Día/Mes/Año", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=70, y=450, width=120)

dolar_bcv = Label(text="Dólar BCV:", font=("Arial"), bg="lightblue" ).place(x=250, y=450)
dolar_bcv_mostrar = Label(text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=350, y=450, width=150)
establecer_monto = Label(text="Establecer Monto:", font=("Arial"), bg="lightblue" ).place(x=200, y=500)
establecer_monto_mostrar = Label(text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=350, y=500, width=150)

monto_establecido = Label(text="Monto Establecido:", font=("Arial"), bg="lightblue" ).place(x=700, y=500)
monto_establecido_mostrar = Label(text="12345678,90 Bs", font=("Arial"), bg="lightblue", relief=SUNKEN ).place(x=850, y=500, width=150)


#RADIO BUTTONS
#Tipos de gasto
r = IntVar()
Radiobutton(root, text="Gastos Ordinarios", variable=r, value=1, bg="lightblue" ).place(x=100, y=140)
Radiobutton(root, text="Anticipo", variable=r, value=2, bg="lightblue" ).place(x=250, y=140)
Radiobutton(root, text="Previsión", variable=r, value=3, bg="lightblue" ).place(x=400, y=140)
Radiobutton(root, text="Gastos Variables", variable=r, value=4, bg="lightblue" ).place(x=100, y=160)
Radiobutton(root, text="Gastos extraordinarios", variable=r, value=5, bg="lightblue" ).place(x=250, y=160)
Radiobutton(root, text="Otros", variable=r, value=6, bg="lightblue" ).place(x=400, y=160)
#Monto(Bs o $USD)
m = IntVar()
Radiobutton(root, text="Bs", variable=m, value=1, bg="lightblue" ).place(x=450, y=220)
Radiobutton(root, text="$", variable=m, value=2, bg="lightblue" ).place(x=400, y=220)



vista_recibo = Entry().place(x=190, y=45, width=200)
nuevo_recibo = Entry().place(x=190, y=80, width=200)
descripcion = Entry().place(x=190, y=180, width=200)
monto = Entry().place(x=190, y=220, width=200)
buscar_item = Entry().place(x=190, y=340, width=200)

def tabla_saldo():
   pass 

root.mainloop()