from tkinter import *
import pyodbc,SQL_Handler,Challenge_viget


class Random_viget(SQL_Handler.SQL_Handler):
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

        #title
        self.Title = Label(self.root, text="Random Phrasal Verb", font=('Helvetica', 32, 'bold'), bg="orange", fg="white",
                           width=23)



        #definition labels
        self.definition_label = Label(self.root, text="Definition:", font=('Rockwell', 22, 'bold'),bg="white")
        self.definition_screen = Label(self.root, text=self.definition,font=('Rockwell', 12),bg="#99e699", width="60", height="4")

        #example labels
        self.example_label = Label(self.root, text="Example:", font=('Rockwell', 22, 'bold'),bg="white")
        self.example_screen = Label(self.root, text=self.definition, font=('Rockwell', 12), bg="#99e699", width="60",
                                       height="6")

        # verb labels
        self.phrasal_verb_label = Label(self.root, text="Phrasal Verb:", font=('Rockwell', 22, 'bold'), bg="white")
        self.phrasal_verb_screen_label = Label(self.root, text=self.verb, font=('Rockwell', 12), bg="#99e699",
                                               width="60", height="2")




        #buttons
        self.random_button = Button(self.root, text = "RANDOM",height=2,width=12,font=('Rockwell', 12, 'bold'),bg = "#b300b3",
                                    fg = "white",command = self.display_random_phrasal_verb)



        # footer
        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12, 'bold'),
                                  bg="black", fg="white", width=60, height=2)

        #all items grid
        self.Title.grid(row=0, column=0, columnspan=4)

        self.phrasal_verb_label.grid(row=1, column=0, columnspan=4,pady=10, padx=20)
        self.phrasal_verb_screen_label.grid(row=2, column=0, columnspan=4,pady=10, padx=20)

        self.definition_label.grid(row=3, column=0, columnspan=4,pady=10, padx=20)
        self.definition_screen.grid(row=4, column=0, columnspan=4,pady=10, padx=20)

        self.example_label.grid(row=5, column=0, columnspan=4, pady=10, padx=20)
        self.example_screen.grid(row=6, column=0, columnspan=4, pady=10, padx=20)

        self.random_button.grid(row=7, column=0, columnspan=4, pady=10, padx=20)


        self.footer_label.grid(row=8, column=0, columnspan=4, pady=40,)

    def display_random_phrasal_verb(self):
        self.get_random_phrasal_verb()
        self.verb = ""
        self.definition = ""
        self.example = ""
        self.get_random_phrasal_verb()
        self.phrasal_verb_screen_label.config(text=self.verb)
        self.definition_screen.config(text=self.definition)
        self.example_screen.config(text=self.example)







