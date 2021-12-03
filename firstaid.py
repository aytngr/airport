from facility import Facility
class FirstAid(Facility):
    def __init__(self,cost,type):
        super().__init__("First Aid",cost)
        self.type=type
    def display(self):
        print(f" * {self.type}, Cost: {self.cost}", end=" ")


