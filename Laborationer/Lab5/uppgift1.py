from klasser import Pet


p1 = Pet("Snutte")
p1.add_toy("Boll")
p1.add_toy("Hagelbössa")
p1.kind = "katt"

p2 = Pet("Göran")
p2.add_toy("Blyertspenna")
p2.add_toy("Blyertspenna")
p2.kind = "föräldralös"

p3 = Pet("Jonas")
#p3.add_toy("Gaffel")
p3.kind = ("pudel")

list = [p1, p2]

print(p1.kind)
print(p2)
print(p3)
