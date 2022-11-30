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
            "options": [
                "Rent a car",
                "Get a car back",
                "Add a car",
                "Remove a car",
                "List all cars",
                "List all rentable cars",
                "List all rented cars",
                "List all sold cars",
                "List all unsold cars",
                "Exit"
            ]
        }
