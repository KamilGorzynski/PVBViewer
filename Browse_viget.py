from tkinter import *
import tkinter.ttk as ttk
import SQL_Handler


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

        self.search_kind = ""

        self.create_items()
        self.root.mainloop()

    def create_items(self):
        # title
        self.Title = Label(self.root, text="Browse Phrasal Verb", font=('Helvetica', 32, 'bold'), bg="orange",
                           fg="white",
                           width=23)

        #main screen
        self.main_screen = Text(self.root, font=('Rockwell', 12), bg="#99e699", width="60",
                                      height="15")

        #combobox title label
        self.combobox_title_label = Label(self.root,text = "How you want to find?",font=('Rockwell', 22, 'bold'),bg="white")

        #entry
        self.search_entry = Entry(self.root,font=('Rockwell', 18), bg="#99e699",width=15)

        #combobox
        self.cb_value = StringVar
        self.combobox = ttk.Combobox (self.root, textvariable=self.cb_value,values =('Equals','Starts like', 'Contains', 'Ends like'),width=30,)
        self.combobox.current(2)
        self.combobox.bind("<<ComboboxSelected>>",self.on_select_changed)

        self.search_button = Button(self.root, text="SEARCH", height=2, width=12, font=('Rockwell', 12, 'bold'),
                                       bg="#b300b3", fg="white",command = self.search_phrasal_verbs,cursor = "hand2")
        # footer
        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12, 'bold'),
                                  bg="black", fg="white", width=60, height=2)

        # all items grid
        self.Title.grid(row=0, column=0, columnspan=4)

        self.main_screen.grid(row=3, column=0, columnspan=4, pady=10, padx=20)

        self.combobox_title_label.grid(row=4, column=0, columnspan=4, pady=10, padx=20)


        self.combobox.grid (row=5, column=0, columnspan = 2, pady=10, padx=20)
        self.search_entry.grid (row=5, column=2, columnspan = 2, pady=10, padx=20)

        self.search_button.grid(row=6, column=0, columnspan=4, pady=10, padx=20)

        self.footer_label.grid(row=8, column=0, columnspan=4, pady=40)

    def on_select_changed(self,events):
        self.search_kind = self.combobox.get()


    def search_phrasal_verbs(self):
        sql = self.sql_option(self.search_kind,self.search_entry.get())
        phrasal_list = self.get_phrasal_list(sql)
        self.main_screen.delete(0.0,END)
        self.main_screen.insert(0.0,phrasal_list)




