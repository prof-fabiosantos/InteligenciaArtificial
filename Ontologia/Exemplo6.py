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

class CPU(Thing):
    namespace = onto

class RAM(Thing):
    namespace = onto

class Jogador(Thing):
    namespace = onto

class Computador(Thing):
    namespace = onto

# Definir propriedades
class temGenero(ObjectProperty):
    domain = [Jogo]
    range = [Genero]

class requerRequisito(ObjectProperty):
    domain = [Jogo]
    range = [RequisitoSistema]

class hasCPU(ObjectProperty):
    domain = [RequisitoSistema]
    range = [CPU]

class hasRAM(ObjectProperty):
    domain = [RequisitoSistema]
    range = [RAM]

class possuiJogador(ObjectProperty):
    domain = [Jogo]
    range = [Jogador]

class pertenceJogo(ObjectProperty):
    domain = [Jogador]
    range = [Jogo]

class possuiComputador(ObjectProperty):
    domain = [Jogador]
    range = [Computador]

# Adicionar instâncias e relações
jogo1 = Jogo("Super Mario 3D")
acao_genero = Genero("Acao")

jogo1.temGenero = [acao_genero]

RequisitoMinimo = RequisitoSistema("RequisitoMinimo")
RequisitoMinimo.hasCPU = [CPU("Intel Core i7")]
RequisitoMinimo.hasRAM = [RAM("8GB")]

jogo1.requerRequisito = [RequisitoMinimo]

# Criar instâncias de Jogador e Computador
jogador1 = Jogador("Player1")
computador_jogador1 = Computador("PC Game")
computador_jogador1.hasCPU = [CPU("Intel Core i5")]
computador_jogador1.hasRAM = [RAM("16GB")]

# Estabelecer relações
jogo1.possuiJogador = [jogador1]
jogador1.pertenceJogo = [jogo1]
jogador1.possuiComputador = [computador_jogador1]

# Imprimir informações
print("Jogo:", jogo1.name)
print("Gênero do Jogo:", jogo1.temGenero[0].name)
print("Requisitos do Jogo:")
requisitos_do_jogo = jogo1.requerRequisito[0]

cpu_minima = requisitos_do_jogo.hasCPU[0]
print("CPU Mínima Necessária para Super Mario 3D:", cpu_minima.name)

ram_minima = requisitos_do_jogo.hasRAM[0]
print("RAM Mínima Necessária para Super Mario 3D:", ram_minima.name)

# Supondo que você tenha uma instância de jogador chamada jogador1
jogador1 = Jogador("Player1")

# Verificar se o jogador possui um computador
if jogador1.possuiComputador:
    # Se o jogador possui um computador, obter a instância do computador
    computador_do_jogador1 = jogador1.possuiComputador[0]

    # Verificar se o computador possui uma CPU
    if computador_do_jogador1.hasCPU:
        cpu_do_jogador1 = computador_do_jogador1.hasCPU[0]
        print("CPU do computado do jogador:", cpu_do_jogador1.name)
    else:
        print("O computador do jogador não possui uma CPU.")

    # Verificar se o computador possui RAM
    if computador_do_jogador1.hasRAM:
        ram_do_jogador1 = computador_do_jogador1.hasRAM[0]
        print("RAM do jogador:", ram_do_jogador1.name)
    else:
        print("O computador do jogador não possui RAM.")
else:
    print("O jogador não possui um computador.")


# Verificar se o computador do jogador atende aos requisitos do jogo
if (computador_jogador1.hasCPU[0] == requisitos_do_jogo.hasCPU[0] and
    computador_jogador1.hasRAM[0] == requisitos_do_jogo.hasRAM[0]):
    print("O computador do jogador atende aos requisitos do jogo!")
else:
    print("O computador do jogador não atende aos requisitos do jogo.")

# Salvar a ontologia em um arquivo RDF
onto.save("game_ontology.owl", format="rdfxml")





