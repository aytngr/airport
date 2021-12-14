from Data.contact import Contact
from Data.adress import Adress
class User:
    def __init__(self, name=None, username=None, password=None, contact=None, adress = None):
        self._name = name
        self._username = username
        self._password = password
        self._contact = contact
        self._adress = Adress(adress)

    def register(self,name,username,password,phone,email,adress):
        self._name=name
        self._username=username
        self._password=password
        self._contact=Contact(phone,email)
        self._adress=adress

    def login(self):
        print("Log in...")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == self._username and password == self._password:
            print(f"Hello {self._name}. You succesfully logged in!")
        else:
            print("Username or Password is wrong. Try again")
            self.login()
        print("------------------------")