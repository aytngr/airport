from Airport.airport import Airport
from Flight.businessticket import BusinessTicket
from Flight.economticket import EconomTicket
from User.passenger import Passenger
from Airport.management import Management
from Data.adress import Adress
from Data.contact import Contact
from Flight.airline import Airline
from Flight.flight import Flight
from Data.city import City
from Plane.seat import Seat
from Plane.plane import Plane
from Facility.menu import Menu
from User.admin import Admin
from Facility.firstaid import FirstAid
from Facility.finance import Finance
from Airport.bank import Bank
from Airport.shop import Shop
from Facility.meal import Meal
from Airport.cafe import Cafe

# Adress(city)
user_adress = Adress("Baku")
airport_adress = Adress("Azerbaijan, Baku")
# Contact(phone,email)
user_contact = Contact(557165519, "aytengaraisayeva@gmail.com")
buta_contact = Contact(559874216, "buta@gmail.com")
azal = Contact(124041051, "azal@gmail.com")
# Shop(name,location,open)
accesories_shop = Shop("Accesories Shop", "Terminal 1 - 3rd floor", "Open")
clothing_shop = Shop("Clothing Shop", "Terminal 1 - 3rd floor", "Open")
drug_shop = Shop("Drug Store", "Terminal 1 - 1rd floor", "Closed")
shops = [accesories_shop, clothing_shop, drug_shop]
# Food(name,cost)
soup = Meal("Soup", "5$")
coffee = Meal("Coffee", "1.5$")
hamburger = Meal("Hamburger", "3$")
cola = Meal("Cola", "1$")
# Menu (meals)
mcdonalds_menu = Menu([hamburger,cola])
illy_menu = Menu([soup,coffee])
plane_menu = Menu([hamburger,coffee])
# Cafe(name, offers)
mcdonalds = Cafe("McDonalds", "Terminal 1 - 3rd floor", "Open", mcdonalds_menu)
illy = Cafe("Illy", "Terminal 1 - 3rd floor", "Open", illy_menu)
cafes = [mcdonalds, illy]

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
baku = City("Baku")
# Seat(number,type,status)
seat1, seat2, seat3, seat4 = Seat(1, "regular", True), Seat(2, "business", True), Seat(3, "regular", True), Seat(4, "business", True)
# Plane(name,seats)
plane1, plane2 = Plane("F509", [seat1, seat2]), Plane("A350", [seat3, seat4])
# Ticket(from,to,Plane,seat,date,passenger)
ticket1 = EconomTicket(baku, moscow, plane1, seat1, "11/28/2021")
ticket2 = BusinessTicket(baku, moscow, plane1, seat2, "11/28/2021","Meal Service")
ticket3 = EconomTicket(baku, istanbul, plane2, seat3, "12/28/2021")
ticket4 = BusinessTicket(baku, istanbul, plane2, seat4, "12/28/2021","Meal Service")
istanbul_tickets = [ticket3, ticket4]
moscow_tickets = [ticket1, ticket2]
# Airline(name, contact, tickets)
buta_airline = Airline("Buta Airline", buta_contact, moscow_tickets)
azerbaijan_airline = Airline("Azerbaijan Airlines", azal, istanbul_tickets)
# Flight (name, date, destination,tickets)
flight1 = Flight("BU 9205", buta_airline, "11/28/2021", baku, moscow, moscow_tickets)
flight2 = Flight("TK 333", azerbaijan_airline, "11/28/2021", baku, moscow, moscow_tickets)
flight3 = Flight("BU 708", buta_airline, "12/28/2021", baku, istanbul, istanbul_tickets)
flight4 = Flight("TK 3232", azerbaijan_airline, "12/28/2021", baku, istanbul, istanbul_tickets)
flights=[flight1,flight2,flight3,flight4]
# Creating management
management = Management(flights, [kapital, xalq], [medical_facility1, medical_facility2],
                        [finance_facility1, finance_facility2],shops,cafes)
# Creating Airport
airport = Airport("Haydar Aliyev International Airport", airport_adress, management, facilities, cafes, shops,flights)

# Displaying info about Airport
airport.display_info()
airport.display_schedule()

# Checking and registering user
user = management.check_user()
# Loggining in
user.login()


# Admin stuff
if isinstance(user, Admin):
    user.management = management
    user.generate_and_add_new_flight()
    user.add_ticket_to_flight()
# Passenger stuff
if isinstance(user, Passenger):
    # Searching and choosing flight
    selected_flight = user.search_and_select_flight(airport)
    # Add new flight to schedule

    # Searching and choosing ticket
    user.choose_ticket(selected_flight)
    user.buy_ticket()
    #Add baggage
    baggage1 = user.add_baggage()
    # Checking baggage
    management.check_baggage(baggage1)

    # Shopping

    # Getting first aid
    user.get_firstaid(management)

    # Exchanging currency
    user.exchange_currency(management)

    management.announce_boarding(user)

    #Ordering food
    order1 = user.order_food(plane_menu)
    # Ordering taxi
    # aytn.order_taxi(transport,"Baku, Hazi Aslanov")
    #Adding flight

