from lib.car import Car

class Stock():
    def __init__(self, nb_spot, cars=[]):
        self._nb_spot = nb_spot
        self._cars = list(cars)
        self._parking = [None] * nb_spot

    def add(self, car) -> int:
        """Add a car to the stock"""
        if car in self._cars:
            raise ValueError("Car already in stock")
        elif type(car) != Car:
            raise ValueError("Car is not a car")
        else:
            car.send_back()
            self._cars.append(car)
            position = self._find_clear_position()
            if position is None:
                raise ValueError("No clear position in the stock")
            else:
                self._parking[position] = car
                return self._parking.index(car)

    def rent(self, car) -> int:
        """Rent a car"""
        if car not in self._parking:
            raise ValueError("Car not in the parking")
        elif car.is_rentable():
            car.rent()
            position = self._cars.index(car)
            self._parking[position] = None
            return position
        else:
            raise ValueError("Car not rentable")

    def send_back(self, car) -> int:
        """Send a car back to the stock"""
        if car not in self._cars:
            raise ValueError("Car not in stock")
        else:
            position = self._find_clear_position()
            self._parking[position] = car
            return position

    def _find_clear_position(self) -> int:
        """Find a clear position in the stock"""
        for i, spot in enumerate(self._parking):
            if type(spot) is not Car:
                return i
        raise ValueError("No clear position in the stock")   

    def remove(self, car) -> int:
        """Remove a car from the stock"""
        if car not in self._cars:
            raise ValueError("Car not in stock")
        else:
            self._cars.remove(car)
            position = self._parking.index(car)
            self._parking[position] = None
            return position

    def get_rentable(self) -> list[Car]:
        """Returns a list of all rentable cars"""
        return [car for car in self._parking if car is not None]

    def get_rented(self) -> list[Car]:
        """Returns a list of all rentable cars"""
        rented_cars = []
        for car in self._cars:
            if car.is_rented():
                rented_cars.append(car)
        return rented_cars

    def get_cars(self) -> list[Car]:
        return self._cars
