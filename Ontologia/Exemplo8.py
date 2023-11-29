from owlready2 import *

# Criar uma ontologia vazia
onto_familia = get_ontology("http://www.example.org/family_ontology.owl")

# Definir classes
class Pessoa(Thing):
    namespace = onto_familia

class Pai(Pessoa):
    namespace = onto_familia

class Mae(Pessoa):
    namespace = onto_familia

class Filho(Pessoa):
    namespace = onto_familia

# Definir propriedades
class temPai(ObjectProperty):
    namespace = onto_familia
    domain = [Filho]
    range = [Pai]

class temMae(ObjectProperty):
    namespace = onto_familia
    domain = [Filho]
    range = [Mae]

# Adicionar instâncias e relações
pai1 = Pai("Jose")
mae1 = Mae("Fernanda")
filho1 = Filho("Fabio")

filho1.temPai.append(pai1)
filho1.temMae.append(mae1)

# Métodos para obter pai e mãe de um filho
def obter_pai(filho):
    pais = list(filho.temPai)
    if pais:
        return pais[0].name
    else:
        return None

def obter_mae(filho):
    maes = list(filho.temMae)
    if maes:
        return maes[0].name
    else:
        return None

# Exemplo de uso
print("Pai de "+filho1.name, obter_pai(filho1))
print("Mãe de "+filho1.name, obter_mae(filho1))

# Salvar a ontologia em um arquivo RDF
onto_familia.save("family_ontology.owl", format="rdfxml")

