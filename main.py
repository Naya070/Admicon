from tkinter import *
from interfaz_poo import *
from PIL import ImageTk, Image



def main():
    root = Tk()
    root.wm_title("Admicon")
    app = Ventana_inicio(root)
    app.mainloop()



if __name__== "__main__":
    main()