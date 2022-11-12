import sqlite3 as sl
from tabulate import tabulate


def menu():
    """
    This function will print the main menu and redirect the user to which features of the script he wants to run.
    Show the menu and ask the user for an answer :
    1 will call a function to show all the entries of the DB.
    2 will ask for which car the user want to change state of (sold or rented).
    """
    default_question = tabulate([["Bonjour, que voulez-vous faire ?"], ["1. Afficher toute la base de donnée."],
                                 ["2. Modiffier l'état d'une voiture."]],
                                headers="firstrow", tablefmt="outline")
    user_entered_value = input(default_question + "\n\n")
    if user_entered_value == '1':
        show_all()
    elif user_entered_value == '2':
        id_car = int(input(tabulate([["Quel est l'identifiant de la voiture dont vous voulez modifier ces valeurs ?"]],
                                    tablefmt="outline") + "\n\n"))
        id_car -= 1  # Translate the id from DB (begin by one) to list position (begin by zero).
        show_one(id_car)  # Will show the selected car choose by the user.
        # Will ask for which state to change (EG: not sell => sold)
        state_to_edit = int(
            input(tabulate([["Voulez-vous :"], ["1. Changer l'état de vente ?"], ["2. Changer l'état de location ?"]],
                           headers="firstrow", tablefmt="outline") + "\n\n"))
        state_to_edit += 1  # Translate the id from list position (begin by zero) to DB (begin by one).
        edit_db(id_car, state_to_edit)
    else:
        # Show a message if the value of the user is out of scope.
        print("Veulliez entrer une option valide.")


def connection():
    """
    This function allows the connection to the DB to perform SQL queries.
    :return: An object that allows SQL queries to the DB.
    """
    return sl.connect('dbtest.db')


def get_all_data():
    """
    This function perform a query to get all the date from a table.
    :return: All the form selected table.
    """
    db_data = connection()
    with db_data:
        return db_data.execute("SELECT * FROM voiture")


def write_data(id_car, state_to_edit, new_state):
    """
    This function will change into the DB the selected state of the selected car.
    :param id_car: The id of the car.
    :param state_to_edit: The state that is selected to be change (EG: rent status).
    :param new_state: The new state that will be written into the DB.
    :return: The result of the SQL query.
    """
    db_data = connection()
    id_car += 1  # Translate back the id from list position (begin by zero) to DB (begin by one).
    with db_data:
        if state_to_edit == 2:  # If selected option was to change selling state.
            return db_data.execute(f"UPDATE voiture SET status_vente = {new_state} WHERE id = {id_car};")
        elif state_to_edit == 3:  # If selected option was to change renting state.
            return db_data.execute(f"UPDATE voiture SET status_location = {new_state} WHERE id = {id_car};")


def create_row(data):
    """
    This function will create a row to append showing table.
    :param data: The list of the row that will be translated to human friendly language.
    :return: A new list in human friendly language.
    """
    return [data[0], data[1], "Oui" if data[2] else "Non", "Oui" if data[3] else "Non"]


def show_all():
    """This function will put in shape all the data from the DB and show it."""
    table_for_tabulate = []
    data = get_all_data()
    table_for_tabulate.append(["Identifiant", "Modèle", "Est vendue ?", "Est louée ?"])
    for row in data:
        table_for_tabulate.append(create_row(row))

    print(tabulate(table_for_tabulate, headers='firstrow', tablefmt='fancy_grid', numalign="center"))


def show_one(id_car):
    """This function will put in shape a selected car from the DB and show it."""
    table_for_tabulate = []
    data = get_all_data().fetchall()[id_car]
    table_for_tabulate.append(["Identifiant", "Modèle", "Est vendue ?", "Est louée ?"])
    table_for_tabulate.append(create_row(data))

    print(tabulate(table_for_tabulate, headers='firstrow', tablefmt='fancy_grid', numalign="center"))


def edit_db(id_car, state_to_edit):
    """
    This function process the information to call the function that will actually update the DB and show the car
    with the updated state.
    :param id_car: The id of the car.
    :param state_to_edit: The state that is selected to be change (EG: rent status).
    """
    data = get_all_data().fetchall()[id_car]
    if state_to_edit > 3 or state_to_edit < 2:
        print("Veulliez entrer une option valide.")
    else:
        if data[state_to_edit] == 0:
            write_data(id_car, state_to_edit, 1)
        else:
            write_data(id_car, state_to_edit, 0)
        show_one(id_car)


if __name__ == '__main__':
    """This function only purpose is to call the menu function when the script is executed."""
    menu()
