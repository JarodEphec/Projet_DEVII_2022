import sqlite3 as sl
from lib import Stock, Car

class Core():
    def __init__(self):
        self.db = sl.connect("dbAxelR.db")
        self.cursor = self.db.cursor()
        self.stock = Stock(79)
        self._init_stock()

    def _init_stock(self) -> None:
        """Initialize the stock with the cars in the database"""
        self.cursor.execute("SELECT cars.car_id, model.model_name, brand.brand_name, model.engine, model.car_type, cars.last_safety_inspection, cars.is_sold, cars.is_ranted, cars.position FROM brand, cars, model")
        for row in self.cursor.fetchall():
            self.stock.add(Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    def menu(self) -> set:
        """Returns the menu"""
        return {
            "title": "Menu",
            "description": "Choisissez une option",
            "options": {
                "1": ("Locatiprinton d'une voiture", "rent_car()"),
                "2": ("Restituer une voiture", "send_back()"),
                "3": ("Ajouter une nouvelle voiture", "add_car()"),
                "4": ("Supprimer une voiture du stock", "delete_car()"),
                "5": ("Lister toutes les voitures", "show_all()"),
                "6": ("Lister les voitures disponibles", "show_rentable()"),
                "7": ("Lister les voitures louées", "show_rented()"),
                "8": ("Lister les voitures vendues", "show_solded()"),
                "9": ("Quitter", "exit()")
            }
        }
