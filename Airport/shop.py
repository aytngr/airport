class Shop:
    def __init__(self, name, location,status):
        self.name=name
        self.location=location
        self.status=status
    def __str__(self):
        return f"   {self.name}, {self.location}, {self.status}"