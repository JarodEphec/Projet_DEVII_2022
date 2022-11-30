from lib.position import Position
from datetime import datetime
from datetime import date


class Car:
    def __init__(self, id, model, brand, motor, type, last_vehicle_safety_insurance, sold_status, rental_status,
                 position=Position()):
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
        today_date = datetime.today().strftime('%Y-%m-%d')
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
        return self._last_vehicle_safety_insurance


    def is_ranted(self) -> bool:
        return True if self._rental_status == 1 else False

    def is_sold(self) -> bool:
        return True if self._sold_status == 1 else False
