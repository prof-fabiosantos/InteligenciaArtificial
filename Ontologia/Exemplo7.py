from owlready2 import *
import streamlit as st
import os

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

# Função para adicionar informações sobre jogos
def adicionar_jogo():
    st.header("Adicionar Novo Jogo")
    nome_jogo = st.text_input("Nome do Jogo")
    genero_jogo = st.text_input("Gênero do Jogo")

    # Criar instância de Jogo e Genero
    jogo = Jogo(nome_jogo)
    genero = Genero(genero_jogo)
    jogo.temGenero = [genero]

    # Adicionar propriedade requerRequisito à instância do Jogo
    requisito_jogo = RequisitoSistema(f"Requisito_{nome_jogo}")
    jogo.requerRequisito = [requisito_jogo]

    st.success(f"Jogo {nome_jogo} adicionado com sucesso!")




# Função para adicionar informações sobre requisitos de sistema
def adicionar_requisitos():
    st.header("Adicionar Requisitos de Sistema")
    nome_requisito = st.text_input("Nome do Requisito de Sistema")
    cpu_requisito = st.text_input("CPU Mínima Necessária")
    ram_requisito = st.text_input("RAM Mínima Necessária")

    # Criar instância de RequisitoSistema, CPU e RAM
    requisito = RequisitoSistema(nome_requisito)
    cpu = CPU(cpu_requisito)
    ram = RAM(ram_requisito)
    requisito.hasCPU = [cpu]
    requisito.hasRAM = [ram]

    st.success(f"Requisito {nome_requisito} adicionado com sucesso!")

# Função para adicionar informações sobre jogadores e computadores
def adicionar_jogador_e_computador():
    st.header("Adicionar Jogador e Computador")
    nome_jogador = st.text_input("Nome do Jogador")
    nome_computador = st.text_input("Nome do Computador")
    cpu_computador = st.text_input("CPU do Computador")
    ram_computador = st.text_input("RAM do Computador")

    # Criar instâncias de Jogador, Computador, CPU e RAM
    jogador = Jogador(nome_jogador)
    computador = Computador(nome_computador)
    cpu = CPU(cpu_computador)
    ram = RAM(ram_computador)
    computador.hasCPU = [cpu]
    computador.hasRAM = [ram]
    jogador.possuiComputador = [computador]

    st.success(f"Jogador {nome_jogador} e Computador {nome_computador} adicionados com sucesso!")



# Função para verificar se o PC do jogador atende aos requisitos de pelo menos um jogo
def verificar_requisitos():
    st.header("Verificar Requisitos do Computador")

    # Supondo que você tenha uma instância de jogador chamada jogador1
    nome_jogador_verificacao = st.text_input("Nome do Jogador para Verificação")
    jogador_verificacao = onto.search_one(iri=f"*{nome_jogador_verificacao}*")

    if jogador_verificacao:
        # Certifique-se de que a propriedade possuiComputador está definida para o jogador
        if not hasattr(jogador_verificacao, 'possuiComputador'):
            jogador_verificacao.possuiComputador = []

        # Verificar se o jogador possui um computador
        if jogador_verificacao.possuiComputador:
            computador_verificacao = jogador_verificacao.possuiComputador[0]
            st.write(f"Computador do jogador {nome_jogador_verificacao}: {computador_verificacao.name}")

            # Verificar se o computador atende aos requisitos de pelo menos um jogo
            jogos_compativeis = []
            for jogo in onto.Jogo.instances():
                if jogo.requerRequisito:
                    requisitos_do_jogo = jogo.requerRequisito[0]

                    # Certifique-se de que as propriedades hasCPU e hasRAM estão definidas para requisitos_do_jogo
                    if not hasattr(requisitos_do_jogo, 'hasCPU') or not hasattr(requisitos_do_jogo, 'hasRAM'):
                        continue

                    if (computador_verificacao.hasCPU and requisitos_do_jogo.hasCPU and
                            computador_verificacao.hasCPU[0] == requisitos_do_jogo.hasCPU[0] and
                            computador_verificacao.hasRAM and requisitos_do_jogo.hasRAM and
                            computador_verificacao.hasRAM[0] == requisitos_do_jogo.hasRAM[0]):
                        jogos_compativeis.append(jogo.name)

            if jogos_compativeis:
                st.success(f"O computador do jogador atende aos requisitos dos seguintes jogos: {', '.join(jogos_compativeis)}")
            else:
                st.warning("O computador do jogador não atende aos requisitos de nenhum jogo.")
        else:
            st.warning("O jogador não possui um computador.")
    else:
        st.error("Jogador não encontrado.")

# Criar a interface Streamlit
st.title("Ontologia de Jogos")
opcao = st.sidebar.selectbox("Escolha uma opção", ["Adicionar Jogo", "Adicionar Requisitos", "Adicionar Jogador e Computador", "Verificar Requisitos do Computador"])

if opcao == "Adicionar Jogo":
    adicionar_jogo()
elif opcao == "Adicionar Requisitos":
    adicionar_requisitos()
elif opcao == "Adicionar Jogador e Computador":
    adicionar_jogador_e_computador()
elif opcao == "Verificar Requisitos do Computador":
    verificar_requisitos()
