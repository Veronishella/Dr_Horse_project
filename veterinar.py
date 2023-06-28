import sqlite3

class Veterinar:

    def __init__(self, jmeno, prijmeni, kraj, mesto_1, mesto_2, mesto_3, mobil, email, web):
        self.jmeno=jmeno
        self.prijmeni=prijmeni
        self.kraj=kraj
        self.mesto_1=mesto_1
        self.mesto_2=mesto_2
        self.mesto_3=mesto_3
        self.mobil=mobil
        self.email=email
        self.web=web
        

class Veterinarlist:

    def __init__ (self):
        self.veterinari = []


    def pripojit_databazu (self, zoznam):
        self.conn=sqlite3.connect(zoznam)
        self.cursor=self.conn.cursor()


    def odpojit_databazu(self):
        self.conn.close()


    def nacitat_veterinarov(self):
        self.cursor.execute("SELECT * FROM veterinar")
        rows = self.cursor.fetchall()
        for row in rows:
            self.veterinari.append(Veterinar(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


    def vypis_zoznam_veterinarov(self):
        for veterinar in self.veterinari: 
            print("***************************")
            print("Meno: ", veterinar.jmeno)
            print("Priezvisko: ", veterinar.prijmeni)
            print("Kraj: ", veterinar.kraj)
            print("Mesto 1: ", veterinar.mesto_1)
            print("Mesto 2: ", veterinar.mesto_2)
            print("Mesto 3: ", veterinar.mesto_3)
            print("Mobil: ", veterinar.mobil)
            print("Email: ", veterinar.email)
            print("Web: ", veterinar.web)
            print("***************************")


    def uloz_veterinara (self, jmeno, prijmeni, kraj, mesto_1, mesto_2, mesto_3, mobil, email, web):
        self.cursor.execute("INSERT INTO veterinar (jmeno, prijmeni, kraj, mesto_1, mesto_2, mesto_3, mobil, email, web) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(jmeno, prijmeni, kraj, mesto_1, mesto_2, mesto_3, mobil, email, web))
        self.conn.commit()
        novy_veterinar = Veterinar(jmeno, prijmeni, kraj, mesto_1, mesto_2, mesto_3, mobil, email, web)
        self.veterinari.append(novy_veterinar)
        print("Nový veterinář byl přidán")



    def vyhledej_veterinara_jmeno_prijmeni(self, jmeno=None, prijmeni=None):
        
        jmeno = jmeno.strip().capitalize()   #odstranenie prebytočných medzer a uprava prvého písmena na velké
        prijmeni = prijmeni.strip().capitalize() #odstranenie prebytočných medzer a uprava prvého písmena na velké
        if not jmeno.isalpha():  #pokud uživatel nezadá jmeno - nastav pomlčku
            jmeno = "-"
        if not prijmeni.isalpha(): #pokud uživatel nezadá prijmeno - nastav pomlčku
            prijmeni = "-"

        query = "SELECT * FROM veterinar WHERE jmeno LIKE ? or prijmeni LIKE ?"
        params = ("%{}%".format(jmeno), "%{}%".format(prijmeni))

        self.cursor.execute(query, params)
        rows=self.cursor.fetchall()
        
        if rows:
        
            for row in rows:
                print("Veterináře s daným jménem a příjmením jsou: ")
                print(row)
        else:
            print ("Veterináři s daným jménem a příjmením nejsou.")



    def vyhledej_veterinara_mesto(self, mesto):
        #pošéfovat vypísanie bez uvodzoviek a zátvoriek a v sympatickejšej reprezentácii
        mesto = mesto.strip().capitalize()   #odstranenie prebytočného medzer a uprava prvého písmena na velké
        self.cursor.execute("SELECT * FROM veterinar WHERE mesto_1=? or mesto_2=? or mesto_3=?", (mesto, mesto, mesto))
        rows=self.cursor.fetchall()
        if rows:
            print("Nalezení veterináři: ")
            for row in rows:
                    print(row)
        else:
            print ("Veterináři z daného města nejsou.")




            
    