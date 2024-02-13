import math


class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width*self.height
class circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi *(self.radius**2)
    def calculate_total_area(Shapes):
        total_area = 0
        for Shape in Shapes:
            total_area += shape.calculate_area()
            return total_area
mycircle = circle(9)
myrectangle = Rectangle(15, 10)

print(f"Area of a circle is {mycircle.calculate_area()}")
print(f"Area of rectangle is {myrectangle.calculate_area()}")