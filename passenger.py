import random
from user import User
from baggage import Baggage
from paymentaccount import PaymentAccount
from order import Order
class Passenger(User):
    selected_bank=None
    def __init__(self, name = None, username = None, password = None, contact = None, adress = None, payment_account=None, baggage=None, ticket=None, flight=None, bank=None,orders=None,plane=None):
        super().__init__(name, username, password, contact, adress)
        self.baggage = baggage
        self.ticket = ticket
        self.flight = flight
        self.bank = bank
        self.orders=orders
        self.payment_account=payment_account
        self.plane=plane

    def search_and_select_flight(self,airport):
        """Creates a list of available flights according to passenger's destination"""
        available_flights = []
        user_input=input("If you want to search a flight, type 'search', if not 'exit': ")
        while user_input != 'search' and user_input != 'exit':
            user_input = input("Type 'search' or 'exit': ")
        if user_input=='search':
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
                self.search_and_select_flight(airport)
        elif user_input=='search':
            pass

        return self.flight

    def choose_ticket(self, flight):
        available_tickets = []
        if self.flight is not None:
            print(f"Available tickets on {self.flight.code}: ")
            if flight.tickets is not None:
                for ticket in flight.tickets:
                    available_tickets.append(ticket)
                    print(ticket)
                code_input = input("Enter the seat number of ticket you want to choose: ")
                while self.ticket is None:
                    for t in available_tickets:
                        if int(code_input) == t.seat.number:
                            self.ticket = t
                            self.plane = t.plane
                            break
                    else:
                        code_input = input("Enter available number: ")
                print(f"{self.name} chose this ticket: {self.ticket}, Passenger - {self.name}")
            else:
                print("There is no available tickets for this flight...")

        print("------------------------")

    def buy_ticket(self):
        if self.ticket is not None:
            user_input = input("Do you want to buy('yes' or 'no')?: ")
            if user_input == "yes":
                if self.payment_account is None:
                    self.add_payment_account()
                print("Buying ticket...")
                print(f"Ticket Price: {self.ticket.price}, Your budget: {self.payment_account.budget}")
                self.payment_account.pay(self.ticket.price,'azn')
                print("You successfully paid for ticket...")
                print(f"Current budget: {self.payment_account.budget}")
                print("------------------------")
    def add_payment_account(self):
        while self.payment_account is None:
            print("Adding payment account...")
            azn = int(input("Azn: "))
            dollar = int(input("Dollar: "))
            self.payment_account = PaymentAccount(self.name,{'azn':azn,'dollar':dollar})


    def add_baggage(self):
        user_input = input("For adding baggage, type 'add': ")
        if user_input == "add":
            return Baggage(int(input("Enter your baggage weight: ")))

    def get_firstaid(self, management):
        user_input = input("If you need First Aid, type 'yes': ")
        if user_input == "yes":
            user_input2 = input("Please specify the type('Allergic Reaction', 'Cut or Burn')")
            while user_input2 != "Allergic Reaction" and user_input2 != "Cut or Burn":
                user_input2 = input("Please, enter proper type: ")
            management.send_firstaid(user_input2)
            print("------------------------")

    def select_bank(self, management):
        for bank in management.get_banks():
            print(bank, end=" | ")
        user_input = input("Please select bank(Write the full name):")
        while user_input not in management.get_bank_names():
            user_input = input("There is no such bank, enter again: ")
        for bank in management.get_banks():
            if user_input == bank.name:
                self.selected_bank = bank
                break
        print(f"Selected bank: {self.selected_bank.name}")

    def exchange_currency(self, management):
        user_input = input("For exchange currency, type 'exchange': ")
        if user_input == "exchange":
            if self.payment_account is None:
                self.add_payment_account()
            print(f"{self.name} requested for currency exchange...")
            print(f"Current Budget: {self.payment_account.budget.get('azn')} azn and {self.payment_account.budget.get('dollar')} dollar")
            self.select_bank(management)
            entered_money = int(input("Enter azn amount: "))
            while entered_money > self.payment_account.budget.get('azn'):
                entered_money = int(input("Enter proper azn amount: "))
            exchanged_money = int(entered_money / self.selected_bank.currency)
            self.payment_account.budget["azn"] -= entered_money
            self.payment_account.budget["dollar"] += exchanged_money
            print(f"Exchanging..: Entered money: {entered_money} azn, Exchanged money: {exchanged_money} dollar, Budget: {self.payment_account.budget.get('azn')} azn and {self.payment_account.budget.get('dollar')} dollar")
            print("------------------------")
            return exchanged_money

    def order_food(self, menu):
        if self.plane != None and self.plane.boarded == True:
            ordered_meal = None
            user_input = input("If you want to order food, type 'order': ")
            if user_input == 'order':
                if self.payment_account is None:
                    self.add_payment_account()
                for meal in menu.meals:
                    print(meal)
                order_input = input("Please select one: ")
                while order_input not in menu.get_meal_names():
                    order_input = input("Please enter the meal that is in menu: ")
                for meal in menu.meals:
                    if order_input == meal.name:
                        ordered_meal = meal
                print(f"{self.name} ordered {ordered_meal.name}...")
                order = Order(self, ordered_meal)
                print(order)
                return order

    def order_taxi(self, transport, destination):
        print(f"{self.name} ordered taxi to destination: {destination}")
        print("Available taxies: ")
        for taxi in transport.get_cars():
            print(taxi)
        selected_taxi = random.choice(transport.get_cars())
        print(f"{self.name} picked {selected_taxi.get_model()}")
