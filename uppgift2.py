from klasser import Vector2D as v2D

vektor1 = v2D(4,5)
vektor2 = v2D (3,2)

print(vektor1.add(vektor2))

print (vektor2.get_length())


print (vektor1.add_to_new(vektor2), vektor1, vektor2)


print (vektor2.is_longer_than(vektor1))


print (vektor2.create_unit_vector())
