from TSIS3.classes.task2 import Shape


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length



# rectangle = Rectangle(5, 7)
# print(rectangle.area())
