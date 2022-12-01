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
                    print(f"[ERROR] {menu['options'][option_choose][1]} is not a function")
            else:
                print("Wrong option !")

    def show_all(self):
        """This function will put in shape all the data from the DB and show it."""
        table_for_tabulate = []
        data = self.core.stock.get_cars()
        table_for_tabulate.append(["Identifiant", "Modèle", "Marque", "Moteur", "Type", "Dernier controle technique", "Emplacement dans le parking", "Est vendue ?", "Est louée ?"])
        for row in data:
            table_for_tabulate.append(self.create_row(row))

        print(tabulate(table_for_tabulate, headers='firstrow', tablefmt='fancy_grid', numalign="center"))

    def create_row(self, data):
        """
        This function will create a row to append showing table.
        :param data: The list of the row that will be translated to human friendly language.
        :return: A new list in human friendly language.
        """
        return [data.id, data.model, data.brand, data.motor, data.type, data.last_vehicle_safety_insurance,
                "Oui" if data.is_sold() else "Non", "Oui" if data.is_ranted() else "Non", data.position]

    def exit(self):
        print("Au revoir !")
        exit()
