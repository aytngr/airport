from contact import Contact
from adress import Adress
class User:
    def __init__(self, name=None, username=None, password=None, contact=None, adress = None):
        self.name = name
        self.username = username
        self.password = password
        self.contact = contact
        self.adress = Adress(adress)

    def register(self,name,username,password,phone,email,adress):
        self.name=name
        self.username=username
        self.password=password
        self.contact=Contact(phone,email)
        self.adress=adress

    def login(self):
        print("Log in...")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == self.username and password == self.password:
            print(f"Hello {self.name}. You succesfully logged in!")
        else:
            print("Username or Password is wrong. Try again")
            self.login()
        print("------------------------")