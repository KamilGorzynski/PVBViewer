from tkinter import *
import pyodbc,Welcome_viget,Random_viget,Browse_viget,Add_vidget

class Welcome_viget(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("600x390")
        self.root.config(bg = "white")

        self.create_items()
        self.root.mainloop()



    def create_items(self):
        #title

        self.Title = Label(self.root, text = "PVBViewer",font=('Helvetica', 32, 'bold'), bg = "orange", fg = "white",width = 23)

        #icons
        self.random = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\random.png",width="128",height="128")
        self.browse = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\find.png",width="128",height="128")
        self.add = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\add.png",width="128",height="128")

        #labels

        self.Random_label = Label (self.root, text = "Choose random phrasal verb", bg="white")
        self.Browse_label = Label (self.root, text = "Browse list of phrasal verbs", bg="white")
        self.Add_label = Label (self.root, text = "Add new phrasal verb", bg="white")

        #buttons
        self.Random_button = Button (self.root,image = self.random,bg = "white", command = self.rise_random_vidget)
        self.Browse_button = Button(self.root, image = self.browse,bg = "white",command = self.rise_browse_vidget)
        self.Add_button = Button(self.root,image = self.add,bg = "white",command = self.rise_add_vidget)


        #footer

        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12, 'bold'), bg="black", fg="white",
                           width=60, height = 2)
        #all items grid
        self.Title.grid(row=0, column=0,columnspan=4)

        self.Random_label.grid(row=2, column=0, pady=30, padx=20)
        self.Browse_label.grid(row=2, column=2, pady=30, padx=20)
        self.Add_label.grid(row=2, column=3, pady=30, padx=20)

        self.Random_button.grid(row=3, column=0, pady=20, padx=20)
        self.Browse_button.grid(row=3, column=2, pady=20, padx=20)
        self.Add_button.grid(row=3, column=3, pady=20, padx=20)

        self.footer_label.grid(row=4, column=0, columnspan=4, pady = 40)


    def rise_random_vidget(self):
        random_viget = Random_viget.Random_viget()

    def rise_browse_vidget(self):
        browse_viget = Browse_viget.Browse_viget()

    def rise_add_vidget(self):
        add_viget = Add_vidget.Add_viget()







welcome_viget = Welcome_viget()