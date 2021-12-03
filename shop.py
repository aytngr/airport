class Shop:
    def __init__(self, name, location,open):
        self.__name=name
        self.__location=location
        self.__open=open
    def __str__(self):
        return f"   {self.__name}, {self.__location}, {self.__open}"