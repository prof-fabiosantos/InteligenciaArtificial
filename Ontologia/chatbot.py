from owlready2 import *
import streamlit as st
from streamlit_chat import message as st_message

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
                    print(f" - {acessorio.name}")
                    return f" - {acessorio.name}"
            else:
                print(f"Não há acessórios recomendados para {eletronico}.")
                return f"Não há acessórios recomendados para {eletronico}."
        else:
            print(f"Dispositivo {eletronico} não encontrado na ontologia.")
            return f"Dispositivo não encontrado na ontologia."


st.title("Bot Vendendor de Eletrônicos")

if "ChatHistory" not in st.session_state:
    st.session_state.ChatHistory = []

def generate_answer():
     
    user_message = st.session_state.input_text
    response = recomendar_acessorios(user_message)
    if response != "Dispositivo não encontrado na ontologia.":
        response = "Recomendo você também comprar o acessório: "+response
    else:
        response = "Dispositivo não encontrado na ontologia."
    
    st.session_state.ChatHistory.append({"message": user_message, "is_user": True})
    st.session_state.ChatHistory.append({"message": response, "is_user": False})

def main():  
    
    st.text_input("Qual é o disposito eletrônico que deseja comprar?", key="input_text", on_change=generate_answer)
    for i, chat in enumerate(st.session_state.ChatHistory):
        st_message(**chat, key="Chat"+str(i)) #unpacking
               
        
main()