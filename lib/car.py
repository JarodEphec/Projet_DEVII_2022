from position import Position

class Car():
    def __init__(self, id, model, brand, motor, type, last_vehicle_safety_insurance, position=Position()):
        self.id = id
        self._model = model
        self._brand = brand
        self._motor = motor
        self._type = type
        self._last_vehicle_safety_insurance = last_vehicle_safety_insurance
        self.position = position

    def is_rentable() -> bool:
        pass

    def is_ranted() -> bool:
        pass

    def is_sold() -> bool:
        pass
