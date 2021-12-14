class Adress:
    def __init__(self, city, street=None):
        self.__city = city
        self.__street = street
    def get_city(self):
        return self.__city
    def set_city(self,city):
        self.__city=city
    def get_street(self):
        return self.__street
    def set_street(self,street):
        self.__street=street