from economticket import EconomTicket
from businessticket import BusinessTicket
from flight import Flight
from city import City
from airline import Airline
from plane import Plane
from seat import Seat


class Airport:
    def __init__(self,name,location,management,facilities,cafes,shops,flights):
        self.name=name
        self.location=location
        self.management=management
        self.facilities=facilities
        self.cafes=cafes
        self.shops=shops
        self.flights=flights
    def display_info(self):
        facility_names = []
        print(f"Welcome to {self.name}.")
        print(f"Our facilities: ", end=" ")
        for facility in self.facilities:
            if facility.name not in facility_names:
                print("")
                facility_names.append(facility.name)
                print(f"{facility.name}: ")
            facility.display()

        print("")
        print("Shops in our airport: ")
        for shop in self.shops:
            print(shop)

        print("Cafes in our airport: ")
        for cafe in self.cafes:
            cafe.display()
        print("---------------------------")

    def display_schedule(self):
        print("Displaying flight schedule:")
        for flight in self.flights:
            print(flight)
        print("---------------------------")

    def generate_and_add_new_flight(self):
        user_input = input("If you want to add flight, type 'add', else 'pass': ")
        if user_input == "add":
            print("Adding flight, please insert:")
            new_flight = Flight(input("Code(e.g. 'BU 456'): "), Airline(input("Airline(e.g. 'Buta Airlines'): ")), input("Date(DD/MM/YY): "),City(input("From: ")),City(input("To: ")),[])
            self.flights.append(new_flight)
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
                for flight in self.flights:
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
                    print("Ticket successfully added!:")
                    print(ticket)
                elif user_input == "business":
                    plane = Plane(input("Plane(e.g. 'A550'): "), [])
                    seat = Seat(int(input("Seat: ")),"business")
                    plane.seats.append(seat)
                    ticket=BusinessTicket(target_flight.from_c,target_flight.to_c,plane,seat,target_flight.date,input("Services: "))
                    target_flight.tickets.append(ticket)
                    print("Ticket successfully added!")
                    print(ticket)




