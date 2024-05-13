class Vehicle:
    def __init__(self, id=1, name=None, model=None, year=None, color=None, price=None, latitude=None, longitude=None):
        self.id = id
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"<Vehicle: {self.name} {self.model} {self.year} {self.color} {self.price}>"


