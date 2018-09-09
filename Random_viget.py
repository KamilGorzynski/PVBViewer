from tkinter import *
import pyodbc


class Random_viget(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("465x600")


        self.create_items()
        self.root.mainloop()

    def create_items(self):
        self.Title = Label(self.root, text="PVBViewer", font=('Helvetica', 32, 'bold'), bg="orange", fg="white",
                           width=23)

        # icons
        self.random = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\random.png", width="128",
                                 height="128")
        self.browse = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\find.png", width="128",
                                 height="128")
        self.add = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\add.png", width="128",
                              height="128")

        # labels

        self.Random_label = Label(self.root, text="Choose random phrasal verb", bg="white")
        self.Browse_label = Label(self.root, text="Browse list of phrasal verbs", bg="white")
        self.Add_label = Label(self.root, text="Add new phrasal verb", bg="white")

        # buttons
        self.Random_button = Button(self.root, image=self.random, bg="white", command=self.rise_random_vidget)
        self.Browse_button = Button(self.root, image=self.browse, bg="white", command=self.rise_browse_vidget)
        self.Add_button = Button(self.root, image=self.add, bg="white", command=self.rise_add_vidget)

        # footer

        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12, 'bold'),
                                  bg="black", fg="white",
                                  width=60, height=2)
        # all items grid
        self.Title.grid(row=0, column=0, columnspan=4)



        self.footer_label.grid(row=4, column=0, columnspan=4, pady=40)

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



