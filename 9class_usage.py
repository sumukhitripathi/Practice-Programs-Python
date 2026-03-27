#class usage

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display_attributes(self):
        print("Car Attributes: ", self.brand, self.model, self.color)

obj1 = Car(brand='Toyota', model='Fortuner', color='Black')
obj1.display_attributes()

obj2 = Car(brand='Hyundai', model='Creta', color='Green')
obj2.display_attributes()