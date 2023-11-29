from owlready2 import *

# Criar uma ontologia vazia
onto = get_ontology("http://www.example.org/game_ontology.owl")

# Definir classes
class Jogo(Thing):
    namespace = onto

class Genero(Thing):
    namespace = onto

class RequisitoSistema(Thing):
    namespace = onto

# Definir propriedades
class temGenero(ObjectProperty):
    domain = [Jogo]
    range = [Genero]

class requerRequisito(ObjectProperty):
    domain = [Jogo]
    range = [RequisitoSistema]

# Criar instâncias
meu_jogo = Jogo("MeuJogo")
acao_genero = Genero("Acao")
requisito_minimo = RequisitoSistema("RequisitoMinimo")

# Associar instâncias
meu_jogo.temGenero = [acao_genero]
meu_jogo.requerRequisito = [requisito_minimo]

# Imprimir informações
print("Jogo:", meu_jogo.name)
print("Gênero do Jogo:", meu_jogo.temGenero[0].name)
print("Requisito do Jogo:", meu_jogo.requerRequisito[0].name)

