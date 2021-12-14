from Flight.ticket import Ticket
class EconomTicket(Ticket):
    def __init__(self,from_c, to_c, plane, seat, date):
        super().__init__("Econom Ticket",from_c, to_c, plane, seat, date,270)
    def __str__(self):
        return f"{self.name}: Plane - {self.plane.name}, From - {self.from_c.name}, To - {self.to_c.name}, Seat - {self.seat.number} {self.seat.type}, Price - {self.price} azn"
