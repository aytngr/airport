class PaymentAccount:
    def __init__(self,name, budget):
        self.name=name
        self.budget=budget

    def pay(self,price,currency):
        if self.budget[currency]>=price:
            self.budget[currency]-=price
            return True
        else:
            print("You don't have enough money...")
            return False
