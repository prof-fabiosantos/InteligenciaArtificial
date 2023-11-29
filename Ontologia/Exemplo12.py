from owlready2 import *

# Criar uma ontologia vazia
onto = get_ontology("http://www.example.org/eletronics.owl")

# Definição de classes
class DispositivoEletronico(Thing):
    namespace = onto

class Smartphone(DispositivoEletronico):
    namespace = onto

class Computador(DispositivoEletronico):
    namespace = onto

class Notebook(Computador):
    namespace = onto

class PC(Computador):
    namespace = onto

class Videogame(DispositivoEletronico):
    namespace = onto

class Xbox(Videogame):
    namespace = onto

class PlayStation(Videogame):
    namespace = onto

class Acessorio(Thing):
    namespace = onto

class CapaSmartphone(Acessorio):
    namespace = onto

class Mouse(Acessorio):
    namespace = onto

class Headset(Acessorio):
    namespace = onto

class Pendrive(Acessorio):
    namespace = onto

# Definição de propriedades
class temAcessorio(ObjectProperty):
    namespace = onto
    domain = [DispositivoEletronico]
    range = [Acessorio]

# Adição de indivíduos
smartphone1 = Smartphone("Smartphone iPhone 12")
capa_smartphone1 = CapaSmartphone("Capa para celular")

notebook1 = Notebook("Notebook Avell")
mouse_notebook1 = Mouse("Mouse Logitec")
headset_notebook1 = Headset("Headset Sony")
pendrive_notebook1 = Pendrive("Pendrive 16GB")

pc1 = PC("pc1")
mouse_pc1 = Mouse("mouse_pc1")
headset_pc1 = Headset("headset_pc1")
pendrive_pc1 = Pendrive("pendrive_pc1")

xbox1 = Xbox("xbox1")
playstation1 = PlayStation("playstation1")

# Estabelecimento de associações
smartphone1.temAcessorio.append(capa_smartphone1)

notebook1.temAcessorio.append(mouse_notebook1)
notebook1.temAcessorio.append(headset_notebook1)
notebook1.temAcessorio.append(pendrive_notebook1)

pc1.temAcessorio.append(mouse_pc1)
pc1.temAcessorio.append(headset_pc1)
pc1.temAcessorio.append(pendrive_pc1)

# Salvando a ontologia em um arquivo OWL
onto.save(file="eletronics.owl", format="rdfxml")
