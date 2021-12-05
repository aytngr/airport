class Flight:
    def __init__(self,code, airline,date,from_c,to_c,tickets=None):
        self.code = code
        self.date=date
        self.airline=airline
        self.from_c=from_c
        self.to_c=to_c
        self.tickets=tickets



    def __str__(self):
        return f"{self.code} - Airline: {self.airline.name}, From: {self.from_c.name}, To: {self.to_c.name}, Date: {self.date}"
