from User.user import User
from Flight.economticket import EconomTicket
from Flight.businessticket import BusinessTicket
from Flight.flight import Flight
from Data.city import City
from Flight.airline import Airline
from Plane.plane import Plane
from Plane.seat import Seat

class Admin(User):
    management = None
    def __init__(self, name=None, username=None, password=None, contact=None, adress=None):
        super().__init__(name, username, password, contact, adress)

    def generate_and_add_new_flight(self):
        user_input = input("If you want to add flight, type 'add', else 'pass': ")
        if user_input == "add":
            print("Adding flight, please insert:")
            new_flight = Flight(input("Code(e.g. 'BU 456'): "), Airline(input("Airline(e.g. 'Buta Airlines'): ")), input("Date(DD/MM/YY): "),City(input("From: ")),City(input("To: ")),[])
            self.management.get_flights().append(new_flight)
            print("New flight added to schedule")
            print(new_flight)
        else:
            pass

    def add_ticket_to_flight(self):
        target_flight =None
        user_input = input("If you want to add ticket to flight, type 'add', else 'pass': ")
        if user_input == "add":
            code_input = input("Enter the code of flight that the ticket will belong to: ")
            while target_flight is None:
                for flight in self.management.get_flights():
                    if code_input == flight.code:
                        target_flight = flight
                        break
                else: code_input=input("There is no such flight, enter again: ")
            if target_flight is not None:
                user_input=input(f"Adding ticket to {target_flight.code}, please specify the type of ticket(econom or "
                                 f"business):")
                while user_input != "econom" and user_input !="business":
                    user_input = input("Enter 'econom' or 'business': ")
                if user_input == "econom":
                    plane = Plane(input("Plane(e.g. 'A550'): "),[])
                    seat = Seat(int(input("Seat: ")),"regular")
                    plane.seats.append(seat)
                    ticket=EconomTicket(target_flight.from_c,target_flight.to_c,plane,seat,target_flight.date)
                    target_flight.tickets.append(ticket)
                    print("Ticket successfully added!")
                    print(ticket)
                elif user_input == "business":
                    plane = Plane(input("Plane(e.g. 'A550'): "), [])
                    seat = Seat(int(input("Seat: ")),"business")
                    plane.seats.append(seat)
                    ticket=BusinessTicket(target_flight.from_c,target_flight.to_c,plane,seat,target_flight.date,input("Services: "))
                    target_flight.tickets.append(ticket)
                    print("Ticket successfully added!")
                    print(ticket)