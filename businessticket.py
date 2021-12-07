from ticket import Ticket
class BusinessTicket(Ticket):
    def __init__(self, from_c, to_c, plane, seat, date,service):
        super().__init__("Business Ticket",from_c, to_c, plane, seat, date,350)
        self.service=service
    def __str__(self):
        return f"{self.name}: Plane - {self.plane.name}, From - {self.from_c.name}, To - {self.to_c.name}, Seat - {self.seat.number} {self.seat.type}, Services - {self.service}, Price - {self.price} azn"
