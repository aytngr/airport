from facility import Facility
class Finance(Facility):
    def __init__(self, cost,bank):
        super().__init__("Finance",cost)
        self.bank=bank
    def display(self):

        print(f" * {self.bank.name}", end=" ")