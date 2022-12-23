import csv
from lib import Stock, Car, Client


class Core:
    def __init__(self):
        # self.db = open('dbAxelR.csv', mode='r')
        # self.cursor = self.db.cursor()
        self.stock = Stock(79)
        self._init_stock()

    def _init_stock(self) -> None:
        """Initialize the stock with the cars in the database"""
        csv_reader = csv.DictReader(open('cars.csv', mode='r'))
        for row in csv_reader:
            self.stock.add(
                Car(id=int(row["car_id"]), brand=row["brand_name"], model=row["model_name"], type=row["car_type"],
                    motor=int(row["engine"]), last_vehicle_safety_insurance=row["last_vehicle_safety_insurance"],
                    rental_status=int(row["is_ranted"]), sold_status=int(row["is_sold"]), position=int(row["position"]),
                    deleted_status=int(row["is_deleted"])))

    def menu_delete_car(self) -> dict:
        values = [car for car in self.stock.get_cars()]
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

    def menu(self) -> dict:
        """Returns the menu"""
        return {
            "title": "Menu",
            "description": "Choisissez une option",
            "options": {
                "1": ("Location d'une voiture", "rent_car()"),
                "2": ("Restituer une voiture", "send_back()"),
                "3": ("Ajouter une nouvelle voiture", "add_car()"),
                "4": ("Supprimer une voiture du stock", "menu_delete_car()"),
                "5": ("Lister toutes les voitures", "show_all()"),
                "6": ("Lister les voitures disponibles", "show_rentable()"),
                "7": ("Lister les voitures louées", "show_rented()"),
                "8": ("Lister les voitures vendues", "show_solded()"),
                "9": ("Quitter", "exit()")
            }
        }

    def menu_add_car(self):
        return {
            "title": "Menu ajout d'une voiture",
            "description": "Entrer les données d'une voiture.",
            "inputs": [
                {
                    "type": "str",
                    "text": "Quel est le model de la voiture ?",
                },
                {
                    "type": "str",
                    "text": "Quel est la marque de la voiture ?",
                },
                {
                    "type": "int",
                    "text": "Quel est la puissance du moteur ?",
                },
                {
                    "type": "str",
                    "text": "Quel est le type de la voiture ?",
                },
                {
                    "type": "date",
                    "text": "Quand est la date du dernier controle technique ? (format AAAA-MM-JJ)",
                }
            ]
        }

    """
    def is_brand_in_db(self, brand_test):
        self.cursor.execute(f"SELECT * FROM brand")

        for row in self.cursor.fetchall():
            if row[1] == brand_test:
                return row[0]
        return False
    def new_brand_to_db(self, new_brand_name):
        self.cursor.execute(f"INSERT INTO brand(brand_name) VALUES('{new_brand_name}')")

    def is_model_in_db(self, engine, model_name, brand_id, car_type):
        self.cursor.execute(f"SELECT * FROM model")
        for row in self.cursor.fetchall():
            if row[1] == engine and row[2] == model_name and row[3] == brand_id and row[4] == car_type:
                return row[0]
        return False
    def new_model_to_db(self, engine, model_name, brand_id, car_type):
        self.cursor.execute(f"INSERT INTO model(engine, model_name, brand_id, car_type) VALUES('{engine}','{model_name}','{brand_id}','{car_type}')")
    def new_car_to_db(self, new_car):
        if not self.is_brand_in_db(new_car.brand):
            self.new_brand_to_db(new_car.brand)
        if not self.is_model_in_db(new_car.motor, new_car.model, self.is_brand_in_db(new_car.brand), new_car.type):
            self.new_model_to_db(new_car.motor, new_car.model, self.is_brand_in_db(new_car.brand), new_car.type)
        self.cursor.execute(
            f"INSERT INTO cars(model_id, last_safety_inspection, brand_id, car_type) VALUES('{self.is_model_in_db(new_car.motor, new_car.model, self.is_brand_in_db(new_car.brand), new_car.type)}','{new_car.last_vehicle_safety_insurance}','0','{new_car.sold_status}','{new_car.rental_status}','0')")

    """
