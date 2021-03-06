from tkinter import *
import pyodbc,SQL_Handler
from tkinter import messagebox

class Add_viget(SQL_Handler.SQL_Handler):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("600x700")
        self.root.config(bg="white")


        self.create_items()
        self.root.mainloop()

    def create_items(self):

        # title
        self.Title = Label(self.root, text="Add Phrasal Verb", font=('Helvetica', 32, 'bold'), bg="orange", fg="white",
                           width=23)

        # verb labels
        self.phrasal_verb_label = Label(self.root, text="Phrasal Verb:", font=('Rockwell', 22, 'bold'), bg="white")
        self.phrasal_verb_screen = Text(self.root, font=('Rockwell', 12), bg="#99e699",
                                               width="60", height="2")

        # definition labels
        self.definition_label = Label(self.root, text="Definition:", font=('Rockwell', 22, 'bold'), bg="white")
        self.definition_screen = Text(self.root, font=('Rockwell', 12), bg="#99e699", width="60",
                                       height="4")

        # example labels
        self.example_label = Label(self.root, text="Example:", font=('Rockwell', 22, 'bold'), bg="white")
        self.example_screen = Text(self.root,  font=('Rockwell', 12), bg="#99e699", width="60",
                                    height="6")

        # buttons
        self.clear_button = Button(self.root, text="CLEAR ALL", height=2, width=12, font=('Rockwell', 12, 'bold'),
                                 bg="#b300b3", fg="white",command = self.clear_all,cursor = "hand2")

        self.add_button = Button(self.root, text="ADD NEW!", height=2, width=12, font=('Rockwell', 12, 'bold'),
                                    bg="#b300b3",fg="white",command = self.add_new,cursor = "hand2")


        # footer
        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12, 'bold'),
                                  bg="black", fg="white", width=60, height=2)

        # all items grid
        self.Title.grid(row=0, column=0, columnspan=4)

        self.phrasal_verb_label.grid(row=1, column=0, columnspan=4, pady=10, padx=20)
        self.phrasal_verb_screen.grid(row=2, column=0, columnspan=4, pady=10, padx=20)

        self.definition_label.grid(row=3, column=0, columnspan=4, pady=10, padx=20)
        self.definition_screen.grid(row=4, column=0, columnspan=4, pady=10, padx=20)

        self.example_label.grid(row=5, column=0, columnspan=4, pady=10, padx=20)
        self.example_screen.grid(row=6, column=0, columnspan=4, pady=10, padx=20)

        self.clear_button.grid(row=7, column=0, columnspan=2, pady=10, padx=20)
        self.add_button.grid(row=7, column=2, columnspan=2, pady=10, padx=20)


        self.footer_label.grid(row=8, column=0, columnspan=4, pady=40, )



    def clear_all(self):
        self.phrasal_verb_screen.delete(0.0, END)
        self.definition_screen.delete(0.0,END)
        self.example_screen.delete(0.0, END)

    def add_new(self):
        self.set_phrasal_verb()
        self.clear_all()
        messagebox.showinfo(title = "Info", message = "New phrasal verb has been added!")



