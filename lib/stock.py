from lib.car import Car

class Stock():
    def __init__(self, nb_spot, cars=[]):
        self._nb_spot = nb_spot
        self._cars = cars

    def add(self, car) -> None:
        """Add a car to the stock
        
        PRE: car has to be an instance of class Car
        POST: the car is added to the stock
        """
        if car in self._cars:
            raise ValueError("Car already in stock")
        elif type(car) != Car:
            raise ValueError("Car is not a car")
        else:
            self._cars.append(car)

    def rent(self, car) -> int:
        """Rent a car
        
        PRE: car has to be an instance of class Car
        POST: the car is added to the rented car
        """
        if car not in self._cars:
            raise ValueError("Car not in stock")
        elif car.is_rentable():
            car.rent()
            return car.position
        else:
            raise ValueError("Car not rentable")

    def send_back(self, car) -> int:
        """Send a car back to the stock
        
        PRE: car has to be an instance of class Car
        POST: the car is bring back to the stock
        """
        if car not in self._cars:
            raise ValueError("Car not in stock")
        else:
            return self._find_clear_position()

    def _find_clear_position(self) -> int:
        """Find a clear position in the stock
        
        PRE: None
        POST: a free spot is returned
        """
        used_positions = [car.position for car in self._cars if car.position != None]
        for i in range(self._nb_spot):
            if i not in used_positions:
                return i
        raise ValueError("No clear position in the stock")   

    def remove(self, car) -> None:
        """Remove a car from the stock
        
        PRE: car has to be an instance of class Car
        POST: the car is removed to the stock
        """
        if car not in self._cars:
            raise ValueError("Car not in stock")
        else:
            self._cars.remove(car)

    def get_rentable(self) -> list[Car]:
        """Returns a list of all rentable cars
        
        PRE: None
        POST: a list of rentable car is returned
        """
        rentable_cars = []
        for car in self._cars:
            if car.is_rentable():
                rentable_cars.append(car)
        return rentable_cars

    def get_rented(self) -> list[Car]:
        """Returns a list of all rentable cars
        
        PRE: None
        POST: a list of rented car is returned
        """
        rented_cars = []
        for car in self._cars:
            if car.is_sold():
                rented_cars.append(car)
        return rented_cars

    def get_solded(self) -> list[Car]:
        """Returns a list of all solded cars
        
        PRE: None
        POST: a list of solded car is returned
        """
        solded_cars = []
        for car in self._cars:
            if car.is_rented():
                solded_cars.append(car)
        return solded_cars

    def get_cars(self) -> list[Car]:
        return self._cars
