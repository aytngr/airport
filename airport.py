import datetime
import re
from flight import Flight
from city import City
from airline import Airline
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
        user_input = input("If you want to add flight, type 'add': ")
        if user_input == "add":
            print("Adding flight, please insert:")
            new_flight = Flight(input("Code: "), Airline(input("Airline: ")), input("Date(DD/MM/YY): "),City(input("From: ")),City(input("To: ")))
            self.flights.append(new_flight)
            print("New flight added to schedule")
            print(new_flight)


