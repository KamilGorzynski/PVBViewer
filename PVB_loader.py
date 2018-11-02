import pyodbc

class PVB_loader():
    def __init__(self):

        try:
            self.file = open("C:\\Users\Admin\\Desktop\\pvb_file.txt","r")
        except FileNotFoundError:
            print ("Brak pliku na pulpicie!")

        self.create_table()
        self.load_verbs()
        self.file.close()

    def CONNECTION(self):
        con = pyodbc.connect("Driver={SQL Server};"
                               "Server=DESKTOP-UPREPSE\KSERVER;"
                               "Database=PVB_DB;"
                               "Trusted_Connection=yes;")
        return con

    def create_table(self):
        db = self.CONNECTION()
        sql = """Begin tran commit tran
                 create table PVB_list (
                 id int identity primary key,
                 verb varchar(300) not null,
                 definition varchar(300) not null,
                 example varchar(300) not null,)
                 COMMIT TRANSACTION
                 """
        try:
            db.execute(sql)
            print("Table PVB_list created succesfully...")
        except pyodbc.ProgrammingError:
            print("This table already exists!")

        db.close

    def load_verbs(self):

        for lines in self.file:
            row = lines.split('|')
            verb = row[0]
            definition = row[1]
            example = row[2].rstrip("\n")
            db = self.CONNECTION()
            sql = str("Begin tran commit tran INSERT INTO PVB_list (verb,definition,example) VALUES ('{}','{}','{}')  COMMIT TRANSACTION".format(verb,definition,example))
            db.execute(sql)
            db.close
        print('Rows loaded succesfully...')


first_loader = PVB_loader()
