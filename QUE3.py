# Create a class Circle with a radius attribute and methods area() and perimeter(). Use pi = 3.14159.

class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * Circle.pi * self.radius
    
Circle_1 = Circle(5)
print(f"Area: {Circle_1.area()}")  # Output: Area:
