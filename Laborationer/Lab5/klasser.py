import math


class Pet(object):
    def __init__(self, name=""):
        self.name = name
        self.toy = []
        self.kind = ""

    def __str__(self):
        string1 = "{} är en {} som inte har några leksaker."
        string2 = "{} är en {} som har följande leksaker: {}"
        if self.toy == []:
            return string1.format(self.name, self.kind)
        return string2.format(self.name, self.kind, ", ".join(self.toy))

    def add_toy(self, toy):
        if toy not in self.toy:
            self.toy.append(toy)


class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def get_length(self):
        return math.sqrt(((self.x)**2) + ((self.y)**2))

    def add(self, v1):
        self.x += v1.x
        self.y += v1.y
        return (self.x, self.y)

    def add_to_new(self, v1):
        return Vector2D(self.x + v1.x, self.y + v1.y)

    def is_longer_than(self, v1):
        return v1.get_length() < self.get_length()

    def create_unit_vector(self):
        norm_x = self.x / self.get_length()
        norm_y = self.y / self.get_length()
        return Vector2D(norm_x, norm_y)
