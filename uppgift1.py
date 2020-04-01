from klasser import Pet


p1 = Pet ("Snutte")
p1.add_toy ("Boll")
p1.add_toy ("Hagelbössa")
p1.kind = "Katt"

p2 = Pet ("Göran")
p2.add_toy ("Blyertspenna")
p2.add_toy ("Blyertspenna")
p2.kind = "Föräldralös"

p3 = Pet ()
#p3.add_toy("Fork")
p3.kind = ("Pudel")

list = [p1, p2]

print (p2)
