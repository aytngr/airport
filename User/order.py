class Order:
    def __init__(self,client,meal):
        self.client=client
        self.meal=meal
    def __str__(self):
        return f"Order received: {self.client._name} - Seat no:{self.client.get_ticket().seat.number} - {self.meal}"