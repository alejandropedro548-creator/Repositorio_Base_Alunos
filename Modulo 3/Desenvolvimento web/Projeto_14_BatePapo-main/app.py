import json
from pathlib import Path
from datetime import datetime

import streamlit as st


ARQUIVOS_MENSAGENS = Path("mensagens.json")

st.set_page_config(layout="wide", page_icon="💬")

def carregar_mensagens(): ###Buscar as mensagens do arquivo
    if not ARQUIVOS_MENSAGENS.exists():
        return []
    
    try:
        with open(ARQUIVOS_MENSAGENS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return[]

def salvar_mensagens(mensagens): ###Salvar mensagens do arquivo
    with open(ARQUIVOS_MENSAGENS, "w", encoding="utf-8") as arquivo:
        json.dump(mensagens, arquivo, indent=4, ensure_ascii=False)

def adicionar_mensagem(username, mensagem): ###Adicionar mensagens a lista de mensagens 
    mensagens = carregar_mensagens()

    horario = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    mensagens.insert(0, {"time": horario,
                         "username": username,
                         "mensagem": mensagem})
    salvar_mensagens(mensagens)

st.title("Chat De Mensagens Do Ale")

username = st.sidebar.text_input("**Nome de usuário**", key="username",value="Anônimo")


###Área do chat com atualização
@st.fragment(run_every=3)
def renderizar_chat():
    mensagens = carregar_mensagens()

    with st.container(border=True, height=500):
        for msg in mensagens:
            st.write(f"{msg["time"]} - {msg["username"]}: {msg["mensagem"]}")

renderizar_chat()

entrada_mensagem = st.chat_input("Digite uma mensagem")

if entrada_mensagem:
    adicionar_mensagem(username, entrada_mensagem)
    st.rerun()