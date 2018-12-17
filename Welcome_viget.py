from tkinter import *
import Random_viget,Browse_viget,Add_vidget,Challenge_viget

class Welcome_vidget(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("PVBViewer")
        self.root.geometry("729x632")
        self.root.config(bg = "white")

        self.create_items()
        self.root.mainloop()



    def create_items(self):
        #title

        self.Title = Label(self.root, text = "PVBViewer",font=('Rockwell', 32, 'bold'), bg = "orange", fg = "white",width = 26)

        #icons
        self.random = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\random.png",width="128",height="128")
        self.browse = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\find.png",width="128",height="128")
        self.add = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\add.png",width="128",height="128")
        self.challenge = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\challenge.png", width="128",height="128")
        self.question_mark_photo = PhotoImage(file="C:\\Users\\Admin\\PycharmProjects\\PVBViever\\icons\\question_mark.png", width="128", height="128")

        #high labels
        self.Random_label = Label (self.root, text = "Random",font=('Rockwell', 22, 'bold'), bg="white")
        self.Browse_label = Label (self.root, text = "Browse",font=('Rockwell', 22, 'bold'), bg="white")
        self.Add_label = Label (self.root, text = "Add new",font=('Rockwell', 22, 'bold'), bg="white")
        self.Challenge_label = Label (self.root, text = "Challenge",font=('Rockwell', 22, 'bold'), bg="white")

        #buttons
        self.Random_button = Button (self.root,image = self.random,bg = "white", command = self.rise_random_vidget,cursor = "hand2")
        self.Browse_button = Button(self.root, image = self.browse,bg = "white",command = self.rise_browse_vidget,cursor = "hand2")
        self.Add_button = Button(self.root,image = self.add,bg = "white",command = self.rise_add_vidget,cursor = "hand2")
        self.Challenge_button = Button(self.root,image = self.challenge,bg = "white",command = self.rise_challenge_vidget,cursor = "hand2")

        #low labels


        self.Random_label_low = Label(self.root, text="Learn new definitions by choosing random phrasal verb", font=('Rockwell', 12),
                                  bg="#99e699",width="14",height="8",wraplength=100)
        self.Browse_label_low = Label(self.root, text="Browse list of availabled phrasal verbs, find by phrases", font=('Rockwell', 12),
                                  bg="#99e699",width="14",height="8",wraplength=100)
        self.Add_label_low = Label(self.root, text="Add new phrasal verbs providing verb, definition and own example", font=('Rockwell', 12), bg="#99e699",width="14",height="8",wraplength=100)
        self.Challenge_label_low = Label(self.root, text="Check your knowlage, guess phrasal verb", font=('Rockwell', 12), bg="#99e699",width="14",height="8",wraplength=100)


        #footer
        self.footer_label = Label(self.root, text="PVBViewer © All rights reserved", font=('Helvetica', 12), bg="black", fg="white",
                           width=81, height = 2)
        #all items grid
        self.Title.grid(row=0, column=0,columnspan=5)

        self.Random_label.grid(row=2, column=0, pady=30, padx=20)
        self.Browse_label.grid(row=2, column=2, pady=30, padx=20)
        self.Add_label.grid(row=2, column=3, pady=30, padx=20)
        self.Challenge_label.grid(row=2, column=4, pady=30, padx=20)

        self.Random_button.grid(row=3, column=0, pady=20, padx=20)
        self.Browse_button.grid(row=3, column=2, pady=20, padx=20)
        self.Add_button.grid(row=3, column=3, pady=20, padx=20)
        self.Challenge_button.grid(row=3, column=4, pady=20, padx=20)

        self.Random_label_low.grid(row=4, column=0, pady=30, padx=20)
        self.Browse_label_low.grid(row=4, column=2, pady=30, padx=20)
        self.Add_label_low.grid(row=4, column=3, pady=30, padx=20)
        self.Challenge_label_low.grid(row=4, column=4, pady=30, padx=20)

        self.footer_label.grid(row=5, column=0, columnspan=5, pady = 40)


    def rise_random_vidget(self):
        random_viget = Random_viget.Random_viget()

    def rise_browse_vidget(self):
        browse_viget = Browse_viget.Browse_viget()

    def rise_add_vidget(self):
        add_viget = Add_vidget.Add_viget()

    def rise_challenge_vidget(self):
        challenge_viget = Challenge_viget.Challenge_viget()







welcome_viget = Welcome_vidget()