import random
from admin import Admin
from passenger import Passenger
class Management:
    def __init__(self, flights, banks, medical_facilities, finance_facilities,shops,cafes):
        self.__flights = flights
        self.__banks = banks
        self.__medical_facilities = medical_facilities
        self.__finance_facilities = finance_facilities
        self.__shops=shops
        self.__cafes=cafes

    def get_flights(self):
        return self.__flights

    def get_banks(self):
        return self.__banks
    def get_bank_names(self):
        bank_names = []
        for bank in self.__banks:
            bank_names.append(bank.name)
        return bank_names

    def get_medical_facilities(self):
        return self.__medical_facilities

    def get_finance_facilities(self):
        return self.__finance_facilities

    def get_shops(self):
        return self.__shops

    def get_cafes(self):
        return self.__cafes

    def send_firstaid(self, type):
        for facility in self.__medical_facilities:
            if type == facility.type:
                print(f"First aid for {type} sended... Cost: {facility.cost}")

    def check_baggage(self,baggage):
        if baggage is not None:
            print("Checking baggage...")
            if baggage.get_weight() >= 20:
                print("Your baggage's weight is greater that 20 kg. It will cost additional money...")
            else:
                print("Your baggage is under 20 kg. No additional money costs...")
            print("------------------------")

    def announce_boarding(self,passenger):
        if passenger.ticket != None:
            print("Boarding to the plane...")
            passenger.plane.boarded=True
            print("------------------------")

    def check_user(self):
        user_input=input("Register as 'admin' or 'passenger': ")
        while user_input != 'admin' and user_input != 'passenger':
            user_input = input("Please enter 'admin' or 'passenger': ")
        if user_input=="admin":
            print("Registering... ")
            admin = Admin()
            admin.register(input("Name:"),input("Username: "),input("Password: "),input("Phone: "),
                                   input("Email: "),input("Adress: "))
            return admin
        elif user_input=="passenger":
            print("Registering... ")
            passenger = Passenger()
            passenger.register(input("Name:"),input("Username: "),input("Password: "),input("Phone: "),
                                           input("Email: "),input("Adress: "))
            return passenger
