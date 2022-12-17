from tkinter import *
from tkinter import ttk
from lib import Stock, Core
from functools import partial


class Gui:
    def __init__(self):
        self.core = Core()
        self.root = False
        self.creat_gui()
        self.menu()
        self.root.mainloop()

    def creat_gui(self):
        """ Create a GUI window
        PRE : /
        POST : /
        RAISE : Return an error if the window failed to be created
        """
        try:
            self.root = Tk()
            if not self.root:
                raise Exception("Impossible de construire l'interface graphique.")
            self.root.title("Projet_devII")
            self.frm = ttk.Frame(self.root, padding=30)
            self.frm.grid()
        except Exception as error:
            print(error)

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
                if int(key) != 9:
                    print(f"self.{menu['options'][key][1][:-2]}")
                    ttk.Button(self.frm, text=option[0], command=lambda key=key: exec(f"self.{menu['options'][key][1]}")
                    (self), padding=5).grid(column=1, row=int(key) + 1)
            ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=11)
        except Exception as error:
            self.root.destroy()
            self.creat_gui()
            ttk.Label(self.frm, text=error, padding=10).grid(column=1, row=1)
            ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=11)

    def back_to_menu(self):
        """ Call other mothod to show back the main menu"""
        self.root.destroy()
        self.creat_gui()
        self.menu()

    def show_all(self):
        """This function will put in shape all the data from the DB and show it.
        PRE : /
        POST : /
        RAISE : Create an error window if it can not call the get_cars method
        """
        try:
            if self.core.stock.get_cars() == False:
                raise Exception("Imposible de trouver les informations a afficher.")
            data = self.core.stock.get_cars()
            self.root.destroy()
            self.creat_gui()
            ttk.Button(self.frm, text=" <- ", command=lambda: self.back_to_menu(),
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

            self.root.mainloop()
        except Exception as error:
            self.root.destroy()
            self.creat_gui()
            ttk.Label(self.frm, text=error, padding=10).grid(column=1, row=1)
            ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=11)


