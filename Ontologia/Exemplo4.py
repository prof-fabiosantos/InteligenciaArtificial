from owlready2 import *

# Crie uma ontologia
onto = get_ontology("http://test.org/onto.owl")

# Defina classes na ontologia
class Animal(Thing):
    pass

class Mammal(Animal):
    pass

class Cat(Mammal):
    pass

class Dog(Mammal):
    pass

# Adicione indivíduos à ontologia
with onto:
    tom = Cat()
    fido = Dog()

# Raciocínio baseado em casos usando inferência OWL
sync_reasoner()

# Consulta: Obtenha todos os animais na ontologia
for animal in onto.Animal.instances():
    print(f"{animal.name}: {animal}")

# Consulta: Obtenha todos os mamíferos na ontologia
for mammal in onto.Mammal.instances():
    print(f"{mammal.name}: {mammal}")

