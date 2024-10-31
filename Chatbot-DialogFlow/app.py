import streamlit as st
from dialog_flow import enviar_mensagem, PROJECT_ID
from secrets import token_hex
from PIL import Image
from funcoes import desenhar_recibo

st.set_page_config(initial_sidebar_state="collapsed", layout="centered")

#Função para incluir chats na tela
def add_chats():
    for mensagem in st.session_state.mensagens:
        with st.chat_message(mensagem["role"]):
            if type(mensagem["content"]) == Image.Image:
                st.image(mensagem["content"])
            else:
                st.markdown(mensagem["content"])


st.title("🍔Chat Lanchonete!")
st.sidebar.markdown("""
### 🍟Chat Lanchonete
Este chat é apenas um teste e não tem fins comerciais.
""")

#FAZ CONFIGURAÇÕES INICIAIS
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []
    st.session_state.finalizado = False
    st.session_state["id_sessao"] = token_hex(6)

    with st.chat_message("assistant"):
        st.markdown("Olá")

#Se o pedido foi criado
if st.session_state.get("finalizado"):
    #Ativando o modo finalizado
    enviar_mensagem(credenciais=PROJECT_ID, session_id=st.session_state["id_sessao"], mensagem="#pedido_finalizado_#")
    #Incluindo dados no chat
    st.session_state.mensagens.append({"role": "ai", "content":"---"})
    st.session_state.mensagens.append({"role": "ai", "content": "Seu pedido foi: "})
    for i, item in enumerate(st.session_state.get("pedido")):
        if not item['acompanhamento']:
            item["acompanhamento"] = "Sem acompanhamentos..."
        if not item['observacoes']:
            item['observacoes'] = "Sem observações..."
        valores = ['lanche', 'acompanhamento', 'bebida', 'observacoes']
        st.session_state.mensagens.append({"role": "ai",
                                            "content": desenhar_recibo(num_pedido=i, total=item["valor"], qtd = item['quantidade'] ,itens=[f"{value.capitalize()}: {item[value]}" for value in valores])})
    st.session_state.mensagens.append({"role": "ai", "content": "Para finalizar o pedido digite: #FINALIZAR"})
    st.session_state.mensagens.append({"role": "ai", "content": "Para editar o pedido digite: #EDITAR"})
    st.session_state.finalizado = False

# Pegando Mensagens do Usuário
if prompt := st.chat_input():
    #Adicionando Mensagem
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    #Enviando para o BOT
    resposta = enviar_mensagem(credenciais=PROJECT_ID, session_id=st.session_state["id_sessao"], mensagem=prompt)
    #Adionando Resposta do BOT
    st.session_state.mensagens.append({"role": "ai", "content": resposta})

    #Analisando Resposta do BOT
    if resposta == "#FazerPedido" or resposta == "#EditarPedido":
        st.switch_page(page="pages/Fazer_Pedido.py")
    if resposta == "#FinalizarPedido":
        st.switch_page("pages/Finalizar_Pedido.py")
#INCLUINDO CHATS
add_chats()

