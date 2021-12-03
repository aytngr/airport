class Airport:
    def __init__(self,name,location,management,facilities,cafes,shops):
        self.__name=name
        self.__location=location
        self.__management=management
        self.__facilities=facilities
        self.__cafes=cafes
        self.__shops=shops
    def display_info(self):
        facility_names = []
        print(f"Welcome to {self.__name}.")
        print(f"Our facilities: ", end=" ")
        for facility in self.__facilities:
            if facility.name not in facility_names:
                print("")
                facility_names.append(facility.name)
                print(f"{facility.name}: ")
            facility.display()

        print("")
        print("Shops in our airport: ")
        for shop in self.__shops:
            print(shop)

        print("Cafes in our airport: ")
        for cafe in self.__cafes:
            cafe.display()
        print("---------------------------")