# Create a class Car with attributes make, model, and year. Add a method description() that prints "Year Make Model".

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.year} {self.make} {self.model}")


Car_1 = Car("toyota", "fortuner", 2020)
Car_1.description()  # Output: 2020 toyota fortuner
