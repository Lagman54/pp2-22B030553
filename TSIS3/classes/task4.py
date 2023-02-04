class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def dist(point1, point2):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


# p1 = Point(1, 1)
# p2 = Point(2, 2)
# p1.show()
# p1.move(0, 0)
# p1.show()
# p2.show()
# print(Point.dist(p1, p2))
