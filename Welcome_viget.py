from tkinter import *
import pyodbc,Welcome_viget,Random_viget

class Welcome_viget(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("465x600")


        self.create_items()
        self.root.mainloop()

    def CONNECTION(self):


        con = pyodbc.connect("Driver={SQL Server};"
                               "Server=DESKTOP-UPREPSE\KSERVER;"
                               "Database=###########;"
                               "Trusted_Connection=yes;")
        return con


    def create_items(self):
        #title
        self.Title = Label(self.root, text = "PVBViewer",font=('Helvetica', 12, 'bold'))

        #buttons
        self.Random_button = Button (self.root,text = "Losuj wyrażenie")
        self.Browse_button = Button(self.root, text="Przeglądaj wyrażenia")
        self.Add_button = Button(self.root, text="Dodaj frejzala")

        #all items grid
        self.Title.grid(row=0, column=0,columnspan=4,pady=10,padx=5)

        self.Random_button.grid(row=2, column=1, columnspan=2, pady=20)
        self.Browse_button.grid(row=3, column=1, columnspan=2, pady=20)
        self.Add_button.grid(row=4, column=1, columnspan=2, pady=20)




Welcome_viget = Welcome_viget()