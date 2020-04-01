class Pet (object):
    def __init__ (self, name = ""):
        self.name = name
        self.toy = []
        self.kind = ""

    def __str__(self):
        if self.toy == []:
            return "{} är en {} som inte har några leksaker.".format(self.name, self.kind)
        return "{} är en {} som har följande leksaker: {}".format(self.name, self.kind, ", ".join(self.toy))

    def add_toy(self, toy):
        if toy not in self.toy:
            self.toy.append(toy)
