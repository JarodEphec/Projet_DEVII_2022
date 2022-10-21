# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3 as sl
from tabulate import tabulate

def connection():
    return sl.connect('dbtest.db')

def show_all():
    db_data = connection()
    table_for_tabulate = []
    with db_data:
        data = db_data.execute("SELECT * FROM voiture")
        table_for_tabulate.append(["Identifiant","Modèle","Est vendue ?","Est louée ?"])
        for row in data:
            if row[2] == 0 and row[3] == 0:
                table_for_tabulate.append([row[0], row[1], "Non", "Non" ])
            elif row[2] == 0 and row[3] == 1:
                table_for_tabulate.append([row[0], row[1], "Non", "Oui"])
            elif row[2] == 1 and row[3] == 0:
                table_for_tabulate.append([row[0], row[1], "Oui", "Non"])
            elif row[2] == 1 and row[3] == 1:
                table_for_tabulate.append([row[0], row[1], "Oui", "Oui"])

        print(tabulate(table_for_tabulate, headers='firstrow', tablefmt='fancy_grid', numalign="center"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #show_all()
    default_question = tabulate([["Bonjour, que voulez-vous faire ?"], ["1. Afficher toute la base de donnée."]], headers="firstrow", tablefmt="outline")
    if input(default_question + "\n\n") == '1':
        show_all()
    else:
        print("Veulliez une option valide.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
