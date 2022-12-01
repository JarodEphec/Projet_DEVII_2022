from tkinter import *
from tkinter import ttk
from lib import Stock, Core
from functools import partial


class Gui:
    def __init__(self):
        self.core = Core()
        self.root = Tk()
        self.root.title("Projet_devII")
        self.frm = ttk.Frame(self.root, padding=30)
        self.frm.grid()
        self.menu()
        self.root.mainloop()

    def menu(self):
        menu = self.core.menu()
        ttk.Label(self.frm, text="test", padding=10).grid(column=0, row=0, columnspan=6)
        for key, option in menu["options"].items():
            if int(key) != 9:
                print(f"self.{menu['options'][key][1][:-2]}")
                ttk.Button(self.frm, text=option[0], command=lambda: getattr(self, menu['options'][key][1][:-2])(), padding=5).grid(column=1, row=int(key)+1)
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=11)

    def show_all(self):
        """This function will put in shape all the data from the DB and show it."""
        print("oui")
        data = self.core.stock.get_cars()
        self.root.destroy
        self.root = Tk()
        self.root.title("Projet_devII")
        self.frm = ttk.Frame(self.root, padding=30)
        self.frm.grid()
        print(data)
        """
        for row in data:
            ttk.Label(self.frm, text=row.id, padding=10).grid(column=1, row=row.id)
            ttk.Label(self.frm, text=row.model, padding=10).grid(column=2, row=row.id)
            ttk.Label(self.frm, text=row.brand, padding=10).grid(column=3, row=row.id)
            ttk.Label(self.frm, text=row.motor, padding=10).grid(column=4, row=row.id)
            ttk.Label(self.frm, text=row.type, padding=10).grid(column=5, row=row.id)
            ttk.Label(self.frm, text=row.last_vehicle_safety_insurance, padding=10).grid(column=5, row=row.id)
            ttk.Label(self.frm, text="Oui" if row.is_sold() else "Non", padding=10).grid(column=6, row=row.id)
            ttk.Label(self.frm, text="Oui" if row.is_ranted() else "Non", padding=10).grid(column=7, row=row.id)
            ttk.Label(self.frm, text=row.position, padding=10).grid(column=8, row=data.id)
            """
        self.root.mainloop()

