from klasser import Vector2D as v2D

vektor1 = v2D(4, 5)
vektor2 = v2D(3, 2)

print("Nu körs metoden add med (3,2) och (4,5):")
print(vektor1.add(vektor2))
print("Nu körs metoden get_length på (3,2):")
print(vektor2.get_length())
print("Nu körs metoden add_to_new på (3,2) och (4,5):")
print(vektor1.add_to_new(vektor2))
print("Nu körs metoden is_longer_than på (4,5) och (3,2):")
print(vektor2.is_longer_than(vektor1))
print("Nu körs metoden create_unit_vector på (3,2):")
print(vektor2.create_unit_vector())
