from datetime import datetime
from datetime import date


class Car:
    def __init__(self, id, model, brand, motor, type, last_vehicle_safety_insurance, sold_status, rental_status,
                 position):
        self.id = id
        self._model = model
        self._brand = brand
        self._motor = motor
        self._type = type
        self._last_vehicle_safety_insurance = last_vehicle_safety_insurance
        self._sold_status = sold_status
        self._rental_status = rental_status
        self.position = position

    def is_rentable(self) -> bool:
        """ Tell if the car is retable or not, the car is rentable if it's safety check is due to over 30 days
        return true if the date of today minus the date of the last check lower than 335 if not return false
        PRE : /
        POST : /
        RAISE : Return an error if the date format is wrong
        """
        try:

            # formatting the date using strptime() function
            datetime.strptime(self._last_vehicle_safety_insurance, '%Y-%m-%d')

        except ValueError:
            print("Format incorrect, il devrait etre AAAA-MM-JJ")
        today_date = datetime.today().strftime('%Y-%m-%d')
        # prepare the data to be formatted in a number
        d0 = date(int(today_date[:4]), int(today_date[5:7]), int(today_date[8:10]))
        d1 = date(int(self._last_vehicle_safety_insurance[:4]), int(self._last_vehicle_safety_insurance[5:7]),
                  int(self._last_vehicle_safety_insurance[8:10]))
        delta = d0 - d1
        if delta.days >= 335:
            return False
        return True

    @property
    def model(self):
        return self._model

    @property
    def brand(self):
        return self._brand

    @property
    def motor(self):
        return self._motor

    @property
    def type(self):
        return self._type

    @property
    def last_vehicle_safety_insurance(self):
        """ Return the last_vehicle_safety_insurance's string
        PRE : /
        POST : /
        RAISE : Return an error if the date format is wrong
        """
        try:
            # formatting the date using strptime() function
            datetime.strptime(self._last_vehicle_safety_insurance, '%Y-%m-%d')
            return self._last_vehicle_safety_insurance
        except ValueError:
            print("Format incorrect, il devrait etre AAAA-MM-JJ")


    def is_ranted(self) -> bool:
        """ Check if the car is rented
        O is False and 1 is true due to sqlite limitation
        PRE : /
        POST : /
        RAISE : Return an error if the is_ranted value is wrong
        """
        try:
            if type(self._rental_status) == int and (self._rental_status in range(0, 1, 1)):
                return True if self._rental_status == 1 else False
            else:
                raise TypeError(f"La donnée is_ranted pour la voiture avec l'id {self.id}")
        except TypeError as error:
            print(error)
            return None


    def is_sold(self) -> bool:
        """ Check if the car is sold
        O is False and 1 is true due to sqlite limitation
        PRE : /
        POST : /
        RAISE : Return an error if the is_sold value is wrong
        """

        try:
            if type(self._sold_status) == int and (self._sold_status in range(0, 1, 1)):
                return True if self._sold_status == 1 else False
            else:
                raise TypeError(f"La donnée is_sold pour la voiture avec l'id {self.id}")
        except TypeError as error:
            print(error)
            return None
