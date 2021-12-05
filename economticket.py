from ticket import Ticket
class EconomTicket(Ticket):
    def __init__(self,from_c, to_c, plane, seat, date):
        super().__init__("Econom Ticket",from_c, to_c, plane, seat, date)
