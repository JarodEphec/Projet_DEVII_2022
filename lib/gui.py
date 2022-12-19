from tkinter import *
from tkinter import ttk
from lib import Stock, Core
from functools import partial


class Gui:
    def __init__(self):
        self.core = Core()
        self.root = Tk()
        self.create_gui()
        self.menu()
        self.root.mainloop()

    def create_gui(self):
        """ Create a GUI window
        PRE : /
        POST : /
        RAISE : Return an error if the window failed to be created
        """
        try:
            self.root.destroy() 
            self.root = Tk()
            if not self.root:
                raise Exception("Impossible de construire l'interface graphique.")
            self.root.title("Projet_devII")
            self.frm = ttk.Frame(self.root, padding=30)
            self.frm.grid()
        except Exception as error:
            print(error)

    def error(self, error):
        """ Create a GUI window
        PRE : /
        POST : /
        RAISE : Return an error if the window failed to be created
        """
        self.create_gui()
        ttk.Label(self.frm, text=error, padding=10).grid(column=1, row=1)
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=11)

    def menu(self):
        """show the GUI main page, the menu
        PRE : /
        POST : /
        RAISE : Create an error window if it can not call the menu method
        """
        try:
            if self.core.menu() == False:
                raise Exception("Imposible de trouver les informations a afficher.")
            menu = self.core.menu()
            ttk.Label(self.frm, text="test", padding=10).grid(column=0, row=0, columnspan=6)
            for key, option in menu["options"].items():
                if key != '9':
                    print(f"self.{menu['options'][key][1][:-2]}")
                    #self._create_input("button", option[0], int(key) + 1, partial(eval(f"self.{menu['options'][key][1][:-2]}")))
                    ttk.Button(self.frm, text=option[0], command=lambda key=key: exec(f"self.{menu['options'][key][1]}")
                    (self), padding=5).grid(column=1, row=int(key) + 1)
            ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=11)
        except Exception as error:
            self.error(error)

    def back_to_menu(self):
        """ Call other mothod to show back the main menu"""
        self.create_gui()
        self.menu()

    def _create_input(self, type, text, row, values=[]):
        """ Create an input
        PRE : /
        POST : /
        RAISE : Create an error window if it can not call the menu method
        """
        try:
            if type == "str":
                ttk.Label(self.frm, text=text, padding=10).grid(column=1, row=row)
                ttk.Entry(self.frm, width=30).grid(column=2, row=row)
            elif type == "select":
                ttk.Label(self.frm, text=text, padding=10).grid(column=1, row=row)
                ttk.Combobox(self.frm, values=values).grid(column=2, row=row)
            elif type == "button":
                ttk.Button(self.frm, text=text, command=lambda: exec(f"self.{values}")(self), padding=5).grid(column=1, row=row)
            else:
                raise Exception("Impossible de trouver les informations a afficher.")
        except Exception as error:
            self.error(error)

    def menu_add_car(self):
        """ Call other mothod to show the add car page"""
        try:
            self.create_gui()
            menu = self.core.menu_add_car()
            if not menu:
                raise Exception("Impossible de trouver les informations a afficher.")
            ttk.Label(self.frm, text="test", padding=10).grid(column=0, row=0, columnspan=6)
            for key, option in menu["options"].items():
                if int(key) != 9:
                    print(f"self.{menu['options'][key][1][:-2]}")
                    ttk.Button(self.frm, text=option[0], command=lambda key=key: exec(f"self.{menu['options'][key][1]}")
                    (self), padding=5).grid(column=1, row=int(key) + 1)
            ttk.Button(self.frm, text="Supprimer", command=self.root.destroy).grid(column=1, row=11)
        except Exception as error:
            self.error(error)

    def menu_delete_car(self):
        """ Call other method to show the delete car page"""
        try:
            self.create_gui()
            menu = self.core.menu_delete_car()
            if not menu:
                raise Exception("Impossible de trouver les informations a afficher.")
            ttk.Label(self.frm, text=menu['title'], padding=10).grid(column=0, row=0, columnspan=6)
            inputs = menu['inputs']
            for row, input in enumerate(inputs):
                print(input['type'], input['text'], input['values'])
                self._create_input(input['type'], input['text'], row+1, input['values'])
            self._create_input("button", "Retour au menu", len(inputs)+1, self.back_to_menu)
        except Exception as error:
            self.error(error)

    def delete_car(self):
        pass

    def show_all(self):
        """This function will put in shape all the data from the DB and show it.
        PRE : /
        POST : /
        RAISE : Create an error window if it can not call the get_cars method
        """
        try:
            self.create_gui()
            data = self.core.stock.get_cars()
            if not data:
                raise Exception("Imposible de trouver les informations a afficher.")
            ttk.Button(self.frm, text=" <- ", command=self.back_to_menu,
                       padding=5).grid(column=1, row=1)

            for row in data:
                ttk.Label(self.frm, text=row.id, padding=10).grid(column=1, row=row.id + 1)
                ttk.Label(self.frm, text=row.model, padding=10).grid(column=2, row=row.id + 1)
                ttk.Label(self.frm, text=row.brand, padding=10).grid(column=3, row=row.id + 1)
                ttk.Label(self.frm, text=row.motor, padding=10).grid(column=4, row=row.id + 1)
                ttk.Label(self.frm, text=row.type, padding=10).grid(column=5, row=row.id + 1)
                ttk.Label(self.frm, text=row.last_vehicle_safety_insurance, padding=10).grid(column=5, row=row.id + 1)
                ttk.Label(self.frm, text="Oui" if row.is_sold() else "Non", padding=10).grid(column=6, row=row.id + 1)
                ttk.Label(self.frm, text="Oui" if row.is_rented() else "Non", padding=10).grid(column=7, row=row.id + 1)
                ttk.Label(self.frm, text=row.position, padding=10).grid(column=8, row=row.id + 1)

        except Exception as error:
            self.error(error)


