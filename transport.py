class Transport:
    def __init__(self, name, cars):
        self.__name = name
        self.__cars = cars
    def get_cars(self):
        return self.__cars
