
import sqlite3 as sl
from tabulate import tabulate

def menu():
    default_question = tabulate([["Bonjour, que voulez-vous faire ?"], ["1. Afficher toute la base de donnée."],
                                ["2. Modiffier l'état d'une voiture."]],
                                headers="firstrow", tablefmt="outline")
    user_entered_value = input(default_question + "\n\n")
    if user_entered_value == '1':
        show_all()
    elif user_entered_value == '2':
        id_car = int(input(tabulate([["Quel est l'identifiant de la voiture dont vous voulez modifier ces valeurs ?"]], tablefmt="outline") + "\n\n"))
        id_car -= 1
        show_one(id_car)
        state_to_edit = int(input(tabulate([["Voulez-vous :"], ["1. Changer l'état de vente ?"], ["2. Changer l'état de location ?"]],
                                headers="firstrow", tablefmt="outline") + "\n\n"))
        state_to_edit += 1
        edit_DB(id_car, state_to_edit)
    else:
        print("Veulliez entrer une option valide.")
def connection():
    return sl.connect('dbtest.db')

def get_all_data():
    db_data = connection()
    with db_data:
        return db_data.execute("SELECT * FROM voiture")

def write_data(id,state_to_edit, new_state):
    db_data = connection()
    id += 1
    with db_data:
        if state_to_edit == 2:
            return db_data.execute(f"UPDATE voiture SET status_vente = {new_state} WHERE id = {id};")
        elif state_to_edit == 3:
            return db_data.execute(f"UPDATE voiture SET status_location = {new_state} WHERE id = {id};")
def show_all():
    table_for_tabulate = []
    data = get_all_data()
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
def show_one(id):
    table_for_tabulate = []
    data = get_all_data().fetchall()[id]
    table_for_tabulate.append(["Identifiant","Modèle","Est vendue ?","Est louée ?"])
    if data[2] == 0 and data[3] == 0:
        table_for_tabulate.append([data[0], data[1], "Non", "Non" ])
    elif data[2] == 0 and data[3] == 1:
        table_for_tabulate.append([data[0], data[1], "Non", "Oui"])
    elif data[2] == 1 and data[3] == 0:
        table_for_tabulate.append([data[0], data[1], "Oui", "Non"])
    elif data[2] == 1 and data[3] == 1:
        table_for_tabulate.append([data[0], data[1], "Oui", "Oui"])

    print(tabulate(table_for_tabulate, headers='firstrow', tablefmt='fancy_grid', numalign="center"))
def edit_DB(id, state_to_edit):
    data = get_all_data().fetchall()[id]
    if state_to_edit > 2 or state_to_edit < 1:
        print("Veulliez entrer une option valide.")
    else:
        if data[state_to_edit] == 0:
            print(f"{id} {state_to_edit}, 1")
            write_data(id, state_to_edit, 1)
        else:
            print(f"{id} {state_to_edit}, 0")
            write_data(id, state_to_edit, 0)
    show_one(id)

if __name__ == '__main__':
    menu()

