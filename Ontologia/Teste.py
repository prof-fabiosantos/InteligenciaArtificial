from owlready2 import *

# Carregar a ontologia
onto = get_ontology("./eletronics.owl").load()

# Função para recomendar acessórios
def recomendar_acessorios(eletronico):
    with onto:
        # Carregar instância do dispositivo eletrônico
        dispositivo = onto.search_one(iri=f"*#{eletronico}")

        # Verificar se o dispositivo foi encontrado
        if dispositivo:
            # Obter os acessórios associados ao dispositivo
            acessorios = dispositivo.temAcessorio

            # Verificar se há acessórios recomendados
            if acessorios:
                print(f"Acessórios recomendados para {eletronico}:")
                for acessorio in acessorios:
                    print(f" - {acessorio}")
            else:
                print(f"Não há acessórios recomendados para {eletronico}.")
        else:
            print(f"Dispositivo {eletronico} não encontrado na ontologia.")

# Exemplo de uso
recomendar_acessorios("smartphone1")
recomendar_acessorios("notebook1")
recomendar_acessorios("pc1")
recomendar_acessorios("xbox1")
recomendar_acessorios("playstation1")
