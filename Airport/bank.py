class Bank:
    def __init__(self, name, currency):
        self.name=name
        self.currency=currency
    def __str__(self):
        return f"{self.name} - Currency: {self.currency}"