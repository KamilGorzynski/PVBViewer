from tkinter import *
import pyodbc
from tkinter import messagebox

class SQL_Handler(object):
    def CONNECTION(self):
        try:
            con = pyodbc.connect("Driver={SQL Server};"
                                 "Server=DESKTOP-UPREPSE\KSERVER;"
                                 "Database=PVB_DB;"
                                 "Trusted_Connection=yes;")

        except pyodbc.ProgrammingError:
            messagebox.showinfo(title="Warning", message="No connection with data base!")

        else:
            return con


    def get_max(self):              #function returns max id from pvb db
        db = self.CONNECTION()
        cursor = db.cursor()
        sql = str("SELECT MAX(ID) from PVB_list")
        cursor.execute(sql)
        for row in cursor:
            max = row[0]
        db.close()
        return max


    def get_random_phrasal_verb(self):
        import random
        random = random.randint(1, self.get_max())
        db = self.CONNECTION()
        cursor = db.cursor()
        sql = "SELECT verb,definition,example FROM PVB_list WHERE ID = {}".format(random)
        cursor.execute(sql)
        for row in cursor:
            self.verb = row[0]
            self.definition += row[1]
            self.example += row[2]
        db.close()



    def set_phrasal_verb(self):
        db = self.CONNECTION()
        sql = "BEGIN TRAN COMMIT TRAN \
                     INSERT INTO PVB_list (verb,definition,example) \
                     VALUES ('{}','{}','{}') \
                     COMMIT TRAN".format(self.phrasal_verb_screen.get(0.0, END),
                                         self.definition_screen.get(0.0, END),
                                         self.example_screen.get(0.0, END))

        try:
            db.execute(sql)
        except pyodbc.ProgrammingError:
            messagebox.showinfo(title="Warning", message="Cannot find the table!")
        db.close()

    def sql_option(self,cb_value,entry):        #function chooses query depends on value from combobox
        if cb_value == 'Equals':
            sql = "select * from PVB_list WHERE verb = '{}'".format(entry)
            return sql
        elif cb_value == 'Starts like':
            sql = "select * from PVB_list WHERE verb like '{}%'".format(entry)
            return sql
        elif cb_value == 'Contains':
            sql = "select * from PVB_list WHERE verb like '%{}%'".format(entry)
            return sql
        elif cb_value == 'Ends like':
            sql = "select * from PVB_list WHERE verb like '%{}'".format(entry)
            return sql
        else:
            messagebox.showinfo(title="Warning!",message="Unknown value from combobox!")

    def get_phrasal_list(self,sql):
        message = ""
        db = self.CONNECTION()
        cursor = db.cursor()
        cursor.execute(sql)
        for row in cursor:
            verb = row[1]
            definition = row[2]
            example = row[3]
            message += "\t\t\t###{}###\n".format(verb)
            message += "\t\t\t\tDefinition:\n"
            message += "{}\n".format(definition)
            message += "\t\t\t\tExample:\n"
            message += "{}\n\n\n".format(example)
        db.close
        return message





