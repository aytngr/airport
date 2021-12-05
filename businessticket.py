from ticket import Ticket
class BusinessTicket(Ticket):
    def __init__(self, from_c, to_c, plane, seat, date,services):
        super().__init__("Business Ticket",from_c, to_c, plane, seat, date)
        self.services=services