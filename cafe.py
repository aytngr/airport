class Cafe:
    def __init__(self, name, location, status, offers):
        self.name=name
        self.location=location
        self.status=status
        self.offers=offers
    def display(self):
        offers_dict = dict()
        print(f"    '{self.name}': {self.location}, {self.status} Offers: ", end=" ")
        for o in self.offers:
            offers_dict['offer'] = o.name
            offers_dict['cost'] = o.cost
            print(f"{offers_dict.get('offer')} - {offers_dict.get('cost')}",end=" ")
        print("")
