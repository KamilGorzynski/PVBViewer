from tkinter import *
import pyodbc


class Browse_viget(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("465x600")


        self.create_items()
        self.root.mainloop()

    def create_items(self):
        self.label = Label (self.root, text= 'Browse wiget')
        self.label.grid(row=2, column=0, pady=20, padx=20)

    def CONNECTION(self):
        try:
            con = pyodbc.connect("Driver={SQL Server};"
                                 "Server=DESKTOP-UPREPSE\KSERVER;"
                                 "Database=Serwis_bankowy;"
                                 "Trusted_Connection=yes;")

        except pyodbc.ProgrammingError:
            print("Cannot find the table!")

        else:
            return con



