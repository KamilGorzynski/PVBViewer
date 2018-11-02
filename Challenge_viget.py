from tkinter import *
import SQL_Handler,random
from tkinter import messagebox


class Challenge_viget(SQL_Handler.SQL_Handler):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("600x674")
        self.root.config(bg="white")

        # variables from data base
        self.verb = ""
        self.definition = ""




        self.congratulation_tuple = ("Quite nice!",
                                     "Good shot!",
                                     "Great!",
                                     "You were right!",
                                     "Perfect!")

        self.failure_tuple = ("Not this time...",
                              "Try again...",
                              "Wrong...",
                              "You better shape up...",
                              "Try another time...")


        self.create_items()
        self.next_phrasal_verb()
        self.root.mainloop()



    def create_items(self):

        #title
        self.Title = Label(self.root, text="Guess Phrasal Verb!", font=('Helvetica', 32, 'bold'), bg="orange", fg="white",
                           width=23)



        #definition labels
        self.definition_label = Label(self.root, text="Definition", font=('Rockwell', 22, 'bold'),bg="white")
        self.definition_screen = Label(self.root, text=self.definition,font=('Rockwell', 12),bg="#99e699", width="60", height="2")

        #hint labels
        self.hint_button = Button (self.root, text = "Hint",height=2,width=12,font=('Rockwell', 12, 'bold'),bg = "#b300b3",
                                    fg = "white",cursor = "hand2",command = self.get_hint)
        self.hint_label = Label (self.root, text="", font=('Rockwell', 22, 'bold'),bg="white")

        # verb labels
        self.phrasal_verb_label = Label(self.root, text="Guess Phrasal Verb:", font=('Rockwell', 22, 'bold'), bg="white")
        self.phrasal_verb_entry = Entry(self.root,font=('Rockwell', 22), bg="#99e699",width=15)
        # question mark label



        #buttons
        self.clear_button = Button(self.root, text = "CLEAR",height=2,width=12,font=('Rockwell', 12, 'bold'),bg = "#b300b3",
                                    fg = "white",command = self.clear,cursor = "hand2")
        self.guess_button = Button(self.root, text = "GUESS",height=2,width=12,font=('Rockwell',12, 'bold'),bg = "#b300b3",fg = "white",
                                   command = self.guess_phrasal_verb,cursor = "hand2")

        self.next_verb_button = Button(self.root, text="NEXT ONE", height=2, width=12, font=('Rockwell', 12, 'bold'),
                                   bg="#b300b3", fg="white",command = self.next_phrasal_verb,cursor = "hand2")


        # footer
        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12, 'bold'),
                                  bg="black", fg="white", width=60, height=2)

        #all items grid
        self.Title.grid(row=0, column=0, columnspan=4)



        self.definition_label.grid(row=1, column=0, columnspan=4,pady=10, padx=20)
        self.definition_screen.grid(row=2, column=0, columnspan=4,pady=10, padx=20)

        self.hint_button.grid(row=4, column=0, columnspan=4,pady=10, padx=20)
        self.hint_label.grid(row=3, column=0, columnspan=4,pady=10, padx=20)



        self.phrasal_verb_label.grid(row=5, column=0, columnspan=4, pady=10, padx=20)
        self.phrasal_verb_entry.grid(row=6, column=0, columnspan=4, pady=10, padx=20)



        self.clear_button.grid(row=7, column=0, columnspan=2, pady=10, padx=20)
        self.guess_button.grid(row=7, column=2, columnspan=2, pady=10, padx=20)
        self.next_verb_button.grid(row=8, column=0, columnspan=4, pady=10, padx=20)

        self.footer_label.grid(row=9, column=0, columnspan=4, pady=40,)

    def clear(self):
        self.phrasal_verb_entry.delete(0, END)

    def guess_phrasal_verb(self):
        string_to_compare = self.phrasal_verb_entry.get()
        n = string_to_compare.lower()
        if self.verb == n:
            message = random.choice(self.congratulation_tuple)
            messagebox._show(title = "Correct!",message = message)

        elif n == "":
            messagebox._show(title="Correct!", message="Put your verb!")
        else:
            message = random.choice(self.failure_tuple)
            messagebox._show(title="Failure!", message=message)


    def next_phrasal_verb(self):    #function choose random verb, assign verb,def and exmp and display them (without verb)
        self.verb = ""
        self.definition = ""
        self.example = ""
        self.get_random_phrasal_verb()
        self.definition_screen.config(text=self.definition)
        self.hint_label.config(text="")

    def get_hint(self):
        hint_letter = self.verb[0]
        hint = "This verb starts with: {}".format(hint_letter)
        self.hint_label.config(text = hint, fg = "red")




