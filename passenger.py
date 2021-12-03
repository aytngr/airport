import random
from contact import Contact
from order import Order
class Passenger:
    available_flights = []
    available_tickets = []

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
    def search_flight(self, management, city):
        """Creates a list of available flights according to passenger's destination"""

        print(f"{self.name} is searching for flights with destination to {city.name}...")
        print("Available flights are: ")
        for flight in management.get_flights():
            if flight.destination == city:
                self.available_flights.append(flight)
                print(flight)

    def select_flight(self):
        self.flight = random.choice(self.available_flights)
        print(f"{self.name} chose this flight: {self.flight}")
        print("------------------------")
        return self.flight

    def show_tickets(self, flight):
        print(f"Available tickets on {self.flight.code}: ")
        for ticket in flight.tickets:
            self.available_tickets.append(ticket)
            print(ticket)

    def select_ticket(self):
        self.ticket = random.choice(self.available_tickets)
        self.ticket.passenger = self.name
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
        self.bank = random.choice(management.get_banks())
        print(f"Selected bank: {self.bank.name}")

    def exchange_currency(self, management, entered_money):
        print(f"{self.name} requested for currency exchange...")
        print(f"Current Budget: {self.budget.get('azn')} azn and {self.budget.get('dollar')} dollar")
        self.select_bank(management)
        exchanged_money = int(management.exchange_currency(self.bank, entered_money))
        self.budget["azn"] -= entered_money
        self.budget["dollar"] += exchanged_money
        print(f"Exchanging..: Entered money: {entered_money} azn, Exchanged money: {exchanged_money} dollar, Budget: {self.budget.get('azn')} azn and {self.budget.get('dollar')} dollar")
        print("------------------------")
        return exchanged_money

    def pay_money(self,management,amount):
        print(f"Current Budget: {self.budget.get('azn')} azn and {self.budget.get('dollar')} dollar")

    def order_food(self, food):
        print("Ordering food...")
        return Order(self,food)

    def order_taxi(self, transport, destination):
        print(f"{self.name} ordered taxi to destination: {destination}")
        print("Available taxies: ")
        for taxi in transport.get_cars():
            print(taxi)
        selected_taxi = random.choice(transport.get_cars())
        print(f"{self.name} picked {selected_taxi.get_model()}")
