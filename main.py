from airport import Airport
from passenger import Passenger
from management import Management
from adress import Adress
from ticket import Ticket
from contact import Contact
from airline import Airline
from flight import Flight
from city import City
from seat import Seat
from plane import Plane
from baggage import Baggage
from facility import Facility
from firstaid import FirstAid
from finance import Finance
from bank import Bank
from car import Car
from transport import Transport
from shop import Shop
from food import Food
from cafe import Cafe

# Adress(city)
user_adress = Adress("Baku")
airport_adress = Adress("Azerbaijan, Baku")
# Contact(phone,email)
user_contact = Contact(557165519, "aytengaraisayeva@gmail.com")
buta_contact = Contact(559874216, "buta@gmail.com")
turkish_contact = Contact(124041051, "turkishair@gmail.com")
# Shop(name,location,open)
accesories_shop = Shop("Accesories Shop", "Terminal 1 - 3rd floor", "Open")
clothing_shop = Shop("Clothing Shop", "Terminal 1 - 3rd floor", "Open")
drug_shop = Shop("Drug Store", "Terminal 1 - 1rd floor", "Closed")
shops = [accesories_shop, clothing_shop, drug_shop]
# Food(name,cost)
soup = Food("Soup", "5$")
coffee = Food("Coffee", "1.5$")
hamburger = Food("Hamburger", "3$")
cola = Food("Cola", "1$")
# Cafe(name, offers)
mcdonalds = Cafe("McDonalds", [hamburger, cola])
illy = Cafe("Illy", [soup, coffee])
cafes = [mcdonalds, illy]
# Baggage(scale)
baggage1 = Baggage(25)
# Car(model,cost)
eco_taxi = Car("Eco Taxi", "3$")
premium_taxi = Car("Premium Taxi", "5$")
# transport(name,cars)
transport = Transport("Airport Taxi", [eco_taxi, premium_taxi])
# Bank(name,currency)
kapital = Bank("Kapital Bank", 1.65)
xalq = Bank("Xalq Bank", 1.71)
# Childs of Facility class
medical_facility1 = FirstAid("10$", "Allergic Reaction")
medical_facility2 = FirstAid("5$", "Cut or Burn")
finance_facility1 = Finance("1$", kapital)
finance_facility2 = Finance("1.5$", xalq)
facilities = [medical_facility1, medical_facility2, finance_facility1, finance_facility2]

# City(name)
moscow = City("Moscow")
istanbul = City("Istanbul")
# Seat(number,type,status)
seat1, seat2, seat3, seat4 = Seat(1, "econom", True), Seat(2, "business", True), Seat(3, "econom", True), Seat(4, "business", True)
# Plane(name,seats)
plane1, plane2 = Plane("F509", [seat1, seat2]), Plane("A350", [seat3, seat4])
# Ticket(from,to,plane,seat,date,passenger)
ticket1 = Ticket("Ticket 1", user_adress, moscow, plane1, seat1, "11/28/2021")
ticket2 = Ticket("Ticket 2", user_adress, moscow, plane1, seat2, "11/28/2021")
ticket3 = Ticket("Ticket 3", user_adress, istanbul, plane2, seat3, "12/28/2021")
ticket4 = Ticket("Ticket 4", user_adress, istanbul, plane2, seat4, "12/28/2021")
istanbul_tickets = [ticket3, ticket4]
moscow_tickets = [ticket1, ticket2]
# Airline(name, contact, tickets)
buta_airline = Airline("Buta Airline", buta_contact, moscow_tickets)
turkish_airline = Airline("Turkish Airlines", turkish_contact, istanbul_tickets)
# Flight (name, date, destination,tickets)
flight1 = Flight("BU 9205", buta_airline.name, "11/28/2021", moscow, [ticket1, ticket2])
flight2 = Flight("TK 333", turkish_airline.name, "11/28/2021", moscow, [ticket3, ticket4])
flight3 = Flight("BU 708", buta_airline.name, "12/28/2021", istanbul, [ticket1, ticket2])
flight4 = Flight("TK 3232", turkish_airline.name, "12/28/2021", istanbul, [ticket3, ticket4])
flights=[flight1,flight2,flight3,flight4]
# Creating management
management = Management(flights, [kapital, xalq], [medical_facility1, medical_facility2],
                        [finance_facility1, finance_facility2],shops,cafes)
# Creating airport
airport = Airport("Haydar Aliyev International Airport", airport_adress, management, facilities, cafes, shops)

# Passenger(name, username, password, contact, baggage, budget, ticket=None,flight=None, bank=None)
aytn = Passenger()
# aytn = Passenger("Aytn", "aytn", "12345", user_contact, baggage1, {"azn":1000, "dollar":100})

# Registering
aytn.register("Aytan", "aytn", "12345", "0555555555", "example@gmail.com", user_adress, {"azn": 1000, "dollar": 100})

# Logging in
aytn.login("aytn", "12345")

# Displaying info about airport
airport.display_info()

# Searching and choosing flight
aytn.search_flight(management, moscow)
selected_flight = aytn.select_flight()

# Searching and choosing ticket
aytn.show_tickets(selected_flight)
selected_ticket = aytn.select_ticket()

# Checking baggage
management.check_baggage(baggage1)

# Shopping

# Getting first aid
aytn.get_firstaid(management, "Allergic Reaction")

# Exchanging currency
aytn.exchange_currency(management, 100)

management.announce_boarding()

#Ordering food
order1 = aytn.order_food(hamburger)
print(order1)
# Ordering taxi
# aytn.order_taxi(transport,"Baku, Hazi Aslanov")
