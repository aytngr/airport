class Cafe:
    def __init__(self,name,offers):
        self.__name=name
        self.__offers=offers
    def display(self):
        offers_dict = dict()
        print(f"    '{self.__name}':  Offers: ", end=" ")
        for o in self.__offers:
            offers_dict['offer'] = o.name
            offers_dict['cost'] = o.cost
            print(f"{offers_dict.get('offer')} - {offers_dict.get('cost')}",end=" ")
        print("")
