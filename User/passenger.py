
from User.baggage import Baggage
from User.paymentaccount import PaymentAccount
from User.order import Order
from User.user import User


class Passenger(User):
    selected_bank=None
    
    def __init__(self, name = None, username = None, password = None, contact = None, adress = None, payment_account=None, baggage=None, ticket=None, flight=None,orders=None,plane=None):
        super().__init__(name, username, password, contact, adress)
        self.__baggage = baggage
        self.__ticket = ticket
        self.__flight = flight
        self.__orders=orders
        self.__payment_account=payment_account
        self.__plane=plane

    def get_ticket(self):
        return self.__ticket
    def get_plane(self):
        return self.__plane
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
                while self.__flight is None:
                    for f in available_flights:
                        if code_input == f.code:
                            self.__flight = f
                            break
                    else:
                        code_input=input("Enter proper code: ")
                print(f"{self._name} chose this flight: {self.__flight}")
            else:
                print("No flights found on your request")
                self.search_and_select_flight(airport)
        elif user_input=='search':
            pass

        return self.__flight

    def choose_ticket(self, flight):
        available_tickets = []
        if self.__flight is not None:
            print(f"Available tickets on {self.__flight.code}: ")
            if flight.tickets is not None:
                for ticket in flight.tickets:
                    available_tickets.append(ticket)
                    print(ticket)
                code_input = input("Enter the seat number of ticket you want to choose: ")
                while self.__ticket is None:
                    for t in available_tickets:
                        if int(code_input) == t.seat.number:
                            self.__ticket = t
                            self.__plane = t.plane
                            break
                    else:
                        code_input = input("Enter available number: ")
                print(f"{self._name} chose this ticket: {self.__ticket}, Passenger - {self._name}")
            else:
                print("There is no available tickets for this flight...")

        print("------------------------")

    def buy_ticket(self):
        if self.__ticket is not None:
            user_input = input("Do you want to buy('yes' or 'no')?: ")
            if user_input == "yes":
                if self.__payment_account is None:
                    self.add_payment_account()
                print("Buying ticket...")
                print(f"Ticket Price: {self.__ticket.price}, Your budget: {self.__payment_account.budget}")
                if self.__payment_account.pay(self.__ticket.price,'azn'):
                    print("You successfully paid for ticket...")
                else:
                    print("Update your Payment Account: ")
                    self.__payment_account=None
                    self.add_payment_account()
                print(f"Current budget: {self.__payment_account.budget}")
                print("------------------------")
    def add_payment_account(self):
        while self.__payment_account is None:
            print("You don't have Payment Account or needed to be updated. Adding new payment account...")
            azn = int(input("Azn: "))
            dollar = int(input("Dollar: "))
            self.__payment_account = PaymentAccount(self._name,{'azn':azn,'dollar':dollar})


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
            if self.__payment_account is None:
                self.add_payment_account()
            print(f"{self._name} requested for currency exchange...")
            print(f"Current Budget: {self.__payment_account.budget.get('azn')} azn and {self.__payment_account.budget.get('dollar')} dollar")
            self.select_bank(management)
            entered_money = int(input("Enter azn amount: "))
            while entered_money > self.__payment_account.budget.get('azn'):
                entered_money = int(input("Enter proper azn amount: "))
            exchanged_money = int(entered_money / self.selected_bank.currency)
            self.__payment_account.budget["azn"] -= entered_money
            self.__payment_account.budget["dollar"] += exchanged_money
            print(f"Exchanging..: Entered money: {entered_money} azn, Exchanged money: {exchanged_money} dollar, Budget: {self.__payment_account.budget.get('azn')} azn and {self.__payment_account.budget.get('dollar')} dollar")
            print("------------------------")
            return exchanged_money

    def order_food(self, menu):
        if self.__plane != None and self.__plane.boarded == True:
            ordered_meal = None
            user_input = input("If you want to order food, type 'order': ")
            if user_input == 'order':
                if self.__payment_account is None:
                    self.add_payment_account()
                for meal in menu.meals:
                    print(meal)
                order_input = input("Please select one: ")
                while order_input not in menu.get_meal_names():
                    order_input = input("Please enter the meal that is in menu: ")
                for meal in menu.meals:
                    if order_input == meal.name:
                        ordered_meal = meal
                print(f"{self._name} ordered {ordered_meal.name}...")
                order = Order(self, ordered_meal)
                print(order)
                return order


