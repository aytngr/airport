class Ticket:
    def __init__(self, name, from_c, to_c, plane, seat, date, passenger=None):
        self.name = name
        self.passenger = passenger
        self.from_c = from_c
        self.to_c = to_c
        self.plane = plane
        self.seat = seat
        self.date = date

    def __str__(self):
        return f"{self.name}: Plane - {self.plane.name}, From - {self.from_c.city}, To - {self.to_c.name}, Seat - {self.seat.number} {self.seat.type}"
