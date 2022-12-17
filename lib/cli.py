from tabulate import tabulate
from lib import Stock, Core

class Cli():
    def __init__(self):
        self.core = Core()

    def menu(self):
        menu = self.core.menu()
        while True:
            options = ""
            for key, option in menu["options"].items():
                options += f"{key} : {option[0]}\n"
            option_choose = input(f"""
{menu["title"]}
{options}
{menu["description"]} : """)
            if option_choose.isdigit() and int(option_choose)>0 and int(option_choose)<=len(menu["options"]):
                try:
                    exec(f"self.{menu['options'][option_choose][1]}")
                except AttributeError:
                    print(f"[ERROR] '{menu['options'][option_choose][1]}' is not a function")
            else:
                print("Mauvaise option !")

    def rent_car(self):
        pass

    def send_back(self):
        pass

    def add_car(self):
        self.get_new_car()


    def delete_car(self):
        pass

    def show_all(self):
        """This function will put in shape all the data from the DB and show it."""
        self.show_cars(self.core.stock.get_cars())

    def show_rentable(self):
        self.show_cars(self.core.stock.get_rentable())

    def show_rented(self):
        self.show_cars(self.core.stock.get_rented())

    def show_solded(self):
        self.show_cars(self.core.stock.get_solded())

    def show_cars(self, cars):
        """This function will put in shape all the cars in parameter."""
        table_for_tabulate = []
        table_for_tabulate.append(["Identifiant", "Modèle", "Marque", "Moteur", "Type", "Dernier controle technique",
                                   "Emplacement dans le parking", "Est vendue ?", "Est louée ?"])
        for row in cars:
            table_for_tabulate.append(self.create_row(row))
        print(tabulate(table_for_tabulate, headers='firstrow', tablefmt='fancy_grid', numalign="center"))

    def create_row(self, data):
        """
        This function will create a row to append showing table.
        :param data: The list of the row that will be translated to human friendly language.
        :return: A new list in human friendly language.
        """
        return [data.id, data.model, data.brand, data.motor, data.type, data.last_vehicle_safety_insurance,
                "Oui" if data.is_sold() else "Non", "Oui" if data.is_rented() else "Non", data.position]

    def get_new_car(self):
        menu = self.core.menu_add_car()
        new_car_data = []
        for key, data_car in menu["inputs"].items():
            if data_car[2] == 'int':
                new_car_data.append(int(input(f"{key} : {data_car[0]}\n")))
            else :
                new_car_data.append(input(f"{key} : {data_car[0]}\n"))
        table_for_tabulate = []
        table_for_tabulate.append(["Marque", "Modèle", "Type", "Moteur", "Dernier controle technique"])
        table_for_tabulate.append(new_car_data)
        print(tabulate(table_for_tabulate, headers='firstrow', tablefmt='fancy_grid', numalign="center"))
        if input("Voulez-vous vraiment ajouter cette voiture avec ces information ? (O/N)\n") in ['oui','Oui','OUI'
                                                                                ,'o','O','yes','Yes','YES','y','Y']:
            return new_car_data

    def exit(self):
        print("Au revoir !")
        exit()
