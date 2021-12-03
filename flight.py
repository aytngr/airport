class Flight:
    def __init__(self,code, airline,time,destination,tickets):
        self.code = code
        self.time=time
        self.airline=airline
        self.destination=destination
        self.tickets=tickets
    def __str__(self):
        return f"{self.code} - Airline: {self.airline}, Destination: {self.destination.name}, Date: {self.time}"
