import random

import passenger
from contact import Contact
from order import Order
class Passenger:


    selected_bank=None

    def __init__(self, name=None, username=None, password=None, contact=None, baggage=None, budget=None, ticket=None, flight=None, bank=None,orders=None):
        self.name = name
        self.username = username
        self.password = password
        self.contact = contact
        self.baggage = baggage
        self.ticket = ticket
        self.flight = flight
        self.bank = bank
        self.budget = budget
        self.orders=orders
    def register(self,name,username,password,phone,email,adress,budget):
        self.name=name
        self.username=username
        self.password=password
        self.contact=Contact(phone,email)
        self.adress=adress
        self.budget=budget
    def login(self,username, password):
        if username==self.username and password==self.password:
            print(f"Hello {self.name}. You succesfully logged in!")
        print("------------------------")
    def search_and_select_flight(self,airport):
        """Creates a list of available flights according to passenger's destination"""
        available_flights = []
        user_input=input("If you want to search a flight type 'yes', else 'no': ")
        if user_input=='yes':
            print("Searching flight...")
            from_c=input("From: ")
            to_c=input("To: ")
            date = input("Date: ")
            for flight in airport.flights:
                if flight.from_c.name==from_c and flight.to_c.name==to_c and flight.date==date:
                    available_flights.append(flight)
            if len(available_flights) != 0:
                print("Available flights: ")
                for f in available_flights:
                    print(f)

                code_input = input("Enter the code of flight you want to choose: ")

                while self.flight is None:
                    for f in available_flights:
                        if code_input == f.code:
                            self.flight = f
                            break
                    else:
                        code_input=input("Enter proper code: ")
                print(f"{self.name} chose this flight: {self.flight}")
            else:
                print("No flights found on your request")
        elif user_input=='no':
            pass
        return self.flight
    def choose_ticket(self,flight):
        available_tickets = []
        if self.flight is not None:
            print(f"Available tickets on {self.flight.code}: ")
            for ticket in flight.tickets:
                available_tickets.append(ticket)
                print(ticket)
            code_input = input("Enter the seat number of ticket you want to choose: ")
            while self.ticket is None:
                for t in available_tickets:
                    if int(code_input) == t.seat.number:
                        self.ticket = t
                        break
                else:
                    code_input = input("Enter proper code: ")
            print(f"{self.name} chose this ticket: {self.ticket}, Passenger - {self.name}")
        print("------------------------")
    def get_firstaid(self, management, type):
        print(f"{self.name} needs First Aid for {type}")
        management.send_firstaid(type)
        print("------------------------")
    def select_bank(self, management):
        for bank in management.get_banks():
            print(bank, end=" | ")
        print("")
        self.selected_bank = random.choice(management.get_banks())
        print(f"Selected bank: {self.selected_bank.name}")

    def exchange_currency(self, management, entered_money):
        print(f"{self.name} requested for currency exchange...")
        print(f"Current Budget: {self.budget.get('azn')} azn and {self.budget.get('dollar')} dollar")
        self.select_bank(management)
        exchanged_money = int(entered_money / self.selected_bank.currency)
        self.budget["azn"] -= entered_money
        self.budget["dollar"] += exchanged_money
        print(f"Exchanging..: Entered money: {entered_money} azn, Exchanged money: {exchanged_money} dollar, Budget: {self.budget.get('azn')} azn and {self.budget.get('dollar')} dollar")
        print("------------------------")
        return exchanged_money

    def pay_money(self,management,amount):
        print(f"Current Budget: {self.budget.get('azn')} azn and {self.budget.get('dollar')} dollar")

    def order_food(self, food):
        print(f"{self.name} is ordering food...")
        return Order(self,food)

    def order_taxi(self, transport, destination):
        print(f"{self.name} ordered taxi to destination: {destination}")
        print("Available taxies: ")
        for taxi in transport.get_cars():
            print(taxi)
        selected_taxi = random.choice(transport.get_cars())
        print(f"{self.name} picked {selected_taxi.get_model()}")
