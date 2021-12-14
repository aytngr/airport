


class Airport:
    def __init__(self,name,location,management,facilities,cafes,shops,flights):
        self.name=name
        self.location=location
        self.__management=management
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
        print("Shops in our Airport: ")
        for shop in self.shops:
            print(shop)

        print("Cafes in our Airport: ")
        for cafe in self.cafes:
            cafe.display()
        print("---------------------------")

    def display_schedule(self):
        print("Displaying flight schedule:")
        for flight in self.flights:
            print(flight)
        print("---------------------------")






