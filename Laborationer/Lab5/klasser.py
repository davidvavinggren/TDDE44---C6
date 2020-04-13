import math

class Pet (object):

    def __init__ (self, name = ""):
        """Initiera instansen och skicka med namn."""
        self.name = name
        self.toy = []
        self.kind = ""

    def __str__(self):
        """Printa instansvariabler istället för själva instansen
        enligt formatet nedan.
        """
        string1 = "{} är en {} som inte har några leksaker."
        string2 = "{} är en {} som har följande leksaker: {}"
        if self.toy == []:
            return string1.format(self.name, self.kind)
        return string2.format(self.name, self.kind, ", ".join(self.toy))

    def add_toy(self, toy):
        """Lägg till leksak om den inte redan finns."""
        if toy not in self.toy:
            self.toy.append(toy)


class Vector2D(object):
    def __init__ (self, x, y):
        """Initiera instansen och skicka med x- samt y-koordinat."""
        self.x = x
        self.y = y

    def __str__(self):
        """Formatera så att printen ser ut som en vektor."""
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def get_length(self):
        """Beräkna längden på vektorn."""
        return math.sqrt(((self.x)**2) + ((self.y)**2))

    def add(self, v1):
        """Addera x- och y-koordinat till befintlig vektor."""
        self.x += v1.x
        self.y += v1.y
        return (self.x, self.y)

    def add_to_new(self, v1):
        """Addera vektor och returnera ny."""
        return Vector2D (self.x + v1.x, self.y + v1.y)

    def is_longer_than(self, v1):
        """Kalla på get_length för att undersöka längder, returnera sant eller
        falskt."""
        return v1.get_length() < self.get_length()

    def create_unit_vector(self):
        """Skapa enhetsvektor."""
        norm_x = self.x / self.get_length()
        norm_y = self.y / self.get_length()
        return Vector2D(norm_x, norm_y)
