class Order:
    def __init__(self,client,meal):
        self.client=client
        self.meal=meal
    def __str__(self):
        return f"Order received: {self.client.name} - Seat no:{self.client.ticket.seat.number} - {self.meal}"