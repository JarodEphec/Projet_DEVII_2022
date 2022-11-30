from tabulate import tabulate
from lib import Stock, Core

class Cli():
    def __init__(self):
        self.core = Core()

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
