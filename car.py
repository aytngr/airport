class Car:
    def __init__(self,model,cost):
        self.__model=model
        self.__cost=cost
    def get_model(self):
        return self.__model
    def __str__(self):
        return f"{self.__model} - {self.__cost}"