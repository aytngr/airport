class PaymentAccount:
    def __init__(self,name, budget):
        self.name=name
        self.budget=budget
    def pay(self,price,currency):
        if currency=="dollar":
            if self.budget['dollar']>=price:
                self.budget['dollar']-=price

            else:
                print("You don't have enough money...")
        elif currency=='azn':
            if self.budget['azn'] >= price:
                self.budget['azn'] -= price
            else:
                print("You don't have enough money...")

