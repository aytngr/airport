class Ticket:
    def __init__(self, name, from_c, to_c, plane, seat, date, price, passenger=None):
        self.name = name
        self.passenger = passenger
        self.from_c = from_c
        self.to_c = to_c
        self.plane = plane
        self.seat = seat
        self.date = date
        self.price=price