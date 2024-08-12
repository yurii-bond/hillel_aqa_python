
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point has coordinates x: {self.x}, y: {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point1 = Point(3, 4)
point2 = Point(5, 6)

point3 = point1 + point2
point4 = point1.__add__(point2)


print(point1)
print(point2)
print(point3)
print(point4)

print(point3 == point4)