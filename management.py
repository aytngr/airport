import random

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
        print("Checking baggage...")
        if baggage.get_scale() >= 20:
            print("Your baggage's scale is greater that 20 kg. It will cost additional money...")
        else:
            print("Your baggage is under 20 kg. No additional money costs...")
        print("------------------------")

    def announce_boarding(self):
        print("Boarding to the plane...")
        print("------------------------")
