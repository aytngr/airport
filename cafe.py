class Cafe:
    def __init__(self, name, location, status, menu):
        self.name=name
        self.location=location
        self.status=status
        self.menu=menu
    def display(self):
        menu_dict = dict()
        print(f"    '{self.name}': {self.location}, {self.status}, Offers: ", end=" ")
        for meal in self.menu.meals:
            menu_dict['offer'] = meal.name
            menu_dict['cost'] = meal.cost
            print(f"{menu_dict.get('offer')} - {menu_dict.get('cost')}",end=" ")
        print("")
