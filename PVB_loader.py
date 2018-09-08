import pyodbc

class PVB_loader():
    def __init__(self):

        try:
            self.file = open("C:\\Users\Admin\\Desktop\\pvb_file.txt","r")
        except FileNotFoundError:
            print ("Brak pliku na pulpicie!")

    def CONNECTION(self):
        con = pyodbc.connect("Driver={SQL Server};"
                               "Server=DESKTOP-UPREPSE\KSERVER;"
                               "Database=PVB_DB;"
                               "Trusted_Connection=yes;")
        return con

    def load_verbs(self):


        for lines in self.file:
            verb = ""
            definition = ""
            example = ""
            position = 0
            for i in lines:
                if i =="|":
                    break
                else:
                    verb+=i
                    position+=1
            lines2 = lines[position+1:]
            for i in lines2:
                if i =="|":
                    break
                else:
                    definition+=i
                    position+=1
            lines3 = lines[position + 2:]
            for i in lines3:
                example += i





            db = self.CONNECTION()
            sql = str("Begin tran commit tran INSERT INTO PVB_list (verb,definition,example) VALUES ('{}','{}','{}')  COMMIT TRANSACTION".format(verb,definition,example))
            print(sql)
            db.execute(sql)
            db.close




        self.file.close()

first_loader = PVB_loader()
first_loader.load_verbs()