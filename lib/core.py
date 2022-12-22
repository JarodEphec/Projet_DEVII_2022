import sqlite3 as sl
from lib import Stock, Car, Client

class Core():
    def __init__(self):
        self.db = sl.connect("dbAxelR.db")
        self.cursor = self.db.cursor()
        self.stock = Stock(79)
        self._init_stock()

    def _init_stock(self) -> None:
        """Initialize the stock with the cars in the database"""
        self.cursor.execute("SELECT cars.car_id, model.model_name, brand.brand_name, model.engine, model.car_type,"
                            " cars.last_safety_inspection, cars.is_sold, cars.is_ranted, cars.position FROM brand, "
                            "cars, model")
        for row in self.cursor.fetchall():
            self.stock.add(Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    def look_client_information(self):
        """this method is fetching all the data related to the customers in the database
           PRE:/
           POST: a tab is filled with all the customer's information"""
        self.cursor.execute("SELECT client.id, client.name, client.date_of_inscription, client.history, client.email from client ")
        for row in self.cursor.fetchall():
            self.customer.add(Client(row[0], row[1], row[2], row[3], row[4]))

    def menu_delete_car(self) -> dict:
        values = [str(car) for car in self.stock.get_cars()]
        return {
            "title": "Menu",
            "description": "Choisissez une option",
            "inputs": [
                {
                    "type": "select",
                    "text": "Id de la voiture à supprimer",
                    "values": values
                }
            ]
        }

    def menu_remove_client(self, id) :
        """This method shows the user a menu to remove a customer from the database
           PRE : id is an integer
           POST:return the menu to remove the customer from the database"""
        values = [str(Client) for client in self.get_client()]
        return {
            "title": "Supprimer un client",
            "description": "Choisissez une option",
            "inputs": [
                {
                    "type": "select",
                    "text": "Id du client à supprimer",
                    "values": "values" 
                },
                {
                    "type" : "button",
                    "text": "Supprimer",
                    "values": "remove_client()"
                }
            ]
        }

    def menu(self) -> set:
        """Returns the menu"""
        return {
            "title": "Menu",
            "description": "Choisissez une option",
            "options": {
                "1": ("Location d'une voiture", "rent_car()"),
                "2": ("Restituer une voiture", "send_back()"),
                "3": ("Ajouter une nouvelle voiture", "add_car()"),
                "4": ("Supprimer une voiture du stock", "delete_car()"),
                "5": ("Lister toutes les voitures", "show_all()"),
                "6": ("Lister les voitures disponibles", "show_rentable()"),
                "7": ("Lister les voitures louées", "show_rented()"),
                "8": ("Lister les voitures vendues", "show_solded()"),
                "9": ("ajouter un client", "add_client()"),
                "10":("retirer un client", "menu_remove_client()"),
                "11":("modifier le profil d'un client", "modify_client_information()"),
                "12":("Voir la fidélité du client", "is_loyal()"),
                "13": ("Quitter", "exit()")
            }
        }

    def menu_add_car(self):
        return {
            "title": "Menu ajout d'une voiture",
            "description": "Entrer les données d'une voiture.",
            "inputs": [
                {
                    "type": "str",
                    "text": "Quel est la marque de la voiture ?",
                },
                {
                    "type": "str",
                    "text": "Quel est le model de la voiture ?",
                },
                {
                    "type": "str",
                    "text": "Quel est le type de la voiture ?",
                },
                {
                    "type": "int",
                    "text": "Quel est la puissance du moteur ?",
                },
                {
                    "type": "date",
                    "text": "Quand est la date du dernier controle technique ? (format AAAA-MM-JJ)",
                }
            ]
        }