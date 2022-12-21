from lib import History
from datetime import datetime
from datetime import date
import argparse
import sqlite3 as sl



class Client():
    def __init__(self, id, name, email, date_of_inscription ,history=History(), customer=[]):
        self.id = id
        self.name = name
        self._email = email
        self.history = history
        self.customer = customer
        self.date_of_inscription = date_of_inscription
    
    def add_client(self, id, name, date_of_inscription, history, email) :
        """This method allows the user to add a client in the database
            PRE : str
            POST : /
            RAISE : /
            """
        return {
            "title": "Menu ajout d'un client",
            "description": "Entrer les données du client",
            "inputs": [
                {
                    "type": "str",
                    "text": "Quel est le nom et prénom du client ?",
                },
                {
                    "type": "str",
                    "text": "Quelle est la date lors de l'inscription du client ?",
                },
                {
                    "type": "str",
                    "text": "Le client a-t-il déjà fait un achat (laissez vide si aucun achat) ?",
                },
                {
                    "type": "int",
                    "text": "Quelle est l'adresse mail du client  ?",
                }
            ]
          }


    def remove_client(self, values):
        self.cursor.execute(f"DELETE FROM client WHERE id = '{values}'")


    
    def modify_client_information(self) :
        to_modify = int(input("Entrez l'id du profil client à modifier svp :"))
        for i in self.customer :
            if to_modify == int(self.customer[0]) :
                parser = argparse.ArgumentParser(description=' Quel champ souhaitez-vous modifier ? (name ou date_of_inscription ou history ou email')
                parser.add_argument('name', 'date_of_inscription', 'history', 'email', default='name', help='you can either modify the name, the date of inscription, the email or the history')
                args = parser.parse_args()
                if args == 'name' :
                    new_name = input("Quel est le nouveau nom que vous souhaitez entrer ?")
                    self.customer[1] = new_name
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
            """Prenons comme exemple que le prix est inscrit dans la DB
            Le but est d'afficher l'ancienneté du client lorsqu'il souhaite faire un achat, de là le magasinier applique manuellement
            la réduction sur le montant"""
            pass
        else :
            #print("Ce client n'est pas éligible à une promotion par rapport à son ancienneté.)
            pass

    def get_client(self) :
        return self._id