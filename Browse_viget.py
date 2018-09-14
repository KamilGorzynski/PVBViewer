from tkinter import *
import pyodbc,SQL_Handler


class Browse_viget(SQL_Handler.SQL_Handler):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("600x700")
        self.root.config(bg="white")
        # variables from data base
        self.verb = ""
        self.definition = ""
        self.example = ""

        self.create_items()
        self.root.mainloop()

    def create_items(self):
        # title
        self.Title = Label(self.root, text="Random Phrasal Verb", font=('Helvetica', 32, 'bold'), bg="orange",
                           fg="white",
                           width=23)

        # footer
        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12, 'bold'),
                                  bg="black", fg="white", width=60, height=2)

        # all items grid
        self.Title.grid(row=0, column=0, columnspan=4)
        self.footer_label.grid(row=8, column=0, columnspan=4, pady=40)



s = Browse_viget()

