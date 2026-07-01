class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.A, self.B, self.C)

    def distance_on_line(self, point):
        if self.A * point.x + self.B * point.y + self.C == 0:
            return "lies on the line"
        else:
            return "does not lie on the line"


p1 = point(3, 4)
p2 = point(6, 8)

l1 = line(1, -1, 0)

print(p1)
print(p2)

print("Distance between p1 and p2:", p1.distance_to(p2))
print("Distance of p1 from origin:", p1.distance_from_origin())
print("Distance of p2 from origin:", p2.distance_from_origin())

print("Line equation:", l1)

print(l1.distance_on_line(p1))