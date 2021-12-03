class Order:
    def __init__(self,client,food):
        self.client=client
        self.food=food
    def __str__(self):
        return f"Order received: {self.client.name} - Seat no:{self.client.ticket.seat.number} - {self.food.name}"