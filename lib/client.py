from history import History
from lib import Car, Core
from datetime import datetime
from datetime import date
import argparse


class Client():
    def __init__(self, id, name, email, date_of_inscription ,history=History(), customer=[]):
        self.id = id
        self.name = name
        self._email = email
        self.history = history
        self.customer = customer
        self.date_of_inscription = date_of_inscription
    
    def add_client(self, id, name, date_of_inscription, history, email) :
        """This method allows the user to add a client in the database"""
        if name and email in self.customer :
            raise ValueError("Customer profile already exists")
        else :
            self.customer.append(id, name, date_of_inscription, history, email)

    def remove_client(self, id) :
        """This method allows the user to remove a client from the database"""
        for i in self.customer :
            if self.customer[0] == id:
                self.customer.pop(i)
            else :
                pass

    
    def modify_client_information(self) :
        to_modify = int(input("Entrez l'id du profil client à modifier svp :"))
        for i in self.customer :
            if to_modify == int(self.customer[0]) :
                parser = argparse.ArgumentParser(description=' Quel champ souhaitez-vous modifier ? (name ou date_of_inscription ou history ou email')
                parser.add_argument('name', 'date_of_inscription', 'history', 'email', default='name', help='you can either modify the name, the date of inscription, the email or the history')
                args = parser.parse_args()
                if args == 'name' :
                    new_name = input("Quel est le nouveau nom que vous souhaitez entrer ?")
                    self.customer[1] == new_name
                elif args == "date_of_inscription" :
                    new_date_of_inscription = input("Quelle est la nouvelle date d'inscription que vous souhaitez entrer ?")
                    self.customer[2] =new_date_of_inscription
                elif args == 'history' :
                    new_history = input('Quel hisotrique souhaitez-vous indiquer ?')
                    self.customer[3] = new_history
                elif args =='email' :
                    new_email = input ('Quel est le nouvel email que vous souhaitez indiquer ?')
                    self.customer[4] = new_email
            else :
                pass

    def is_loyal(self) -> bool:
        for i in self.customer[2]:
            today_date = datetime.today().strftime('%Y-%m-%d')
        d0 = date(int(today_date[:4]), int(today_date[5:7]), int(today_date[8:10]))
        d1 = date(int(self.date_of_inscription[:4]), int(self.date_of_inscription[5:7]),
                  int(self.date_of_inscription[8:10]))
        delta = d0 - d1
        if delta >= 355 :
            #à modifier avec les prix
            pass