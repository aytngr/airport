from user import User
from contact import Contact


class Admin(User):
    def __init__(self, name=None, username=None, password=None, contact=None, adress=None):
        super().__init__(name, username, password, contact, adress)
