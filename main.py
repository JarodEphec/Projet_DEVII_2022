import sqlite3 as sl
from tabulate import tabulate
from . import lib


class Car:
    """
    This object create a car with all it's data, some values can be change and write into the DB.
    All the values are private.
    """
    def __init__(self, id_car, name, sale_status, rental_status):
        self.__id_car = id_car
        self.__name = name
        self.__sale_status = sale_status
        self.__rental_status = rental_status

    @property
    def id_car(self):
        return self.__id_car

    @property
    def name(self):
        return self.__name

    @property
    def sale_status(self):
        return self.__sale_status

    def switch_sale_status(self):
        self.__sale_status = 0 if self.__sale_status else 1

    @property
    def rental_status(self):
        return self.__rental_status

    def switch_rental_status(self):
        self.__rental_status = 0 if self.rental_status else 1


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


def write_data(car_to_edit, state_to_edit):
    """
    This function will change into the DB the selected state of the selected car.
    :param car_to_edit: The object where all the specification the car is.
    :param state_to_edit: The state that is selected to be change (EG: rent status).
    :return: The result of the SQL query.
    """
    db_data = connection()
    with db_data:
        if state_to_edit == 2:  # If selected option was to change selling state.
            return db_data.execute(
                f"UPDATE voiture SET status_vente = {car_to_edit.sale_status} WHERE id = {car_to_edit.id_car};")
        elif state_to_edit == 3:  # If selected option was to change renting state.
            return db_data.execute(
                f"UPDATE voiture SET status_location = {car_to_edit.rental_status} WHERE id = {car_to_edit.id_car};")


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
    if state_to_edit == 2:
        car_to_edit = Car(data[0], data[1], data[2], data[3])
        car_to_edit.switch_sale_status()
        write_data(car_to_edit, state_to_edit)
        show_one(id_car)

    elif state_to_edit == 3:
        car_to_edit = Car(data[0], data[1], data[2], data[3])
        car_to_edit.switch_rental_status()
        write_data(car_to_edit, state_to_edit)
        show_one(id_car)
    else:
        print("Veulliez entrer une option valide.")


if __name__ == '__main__':
    """This function only purpose is to call the menu function when the script is executed."""
    menu()
