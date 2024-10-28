import streamlit as st
from groq import Groq
import os
from pathlib import Path

### CHATBOT FURIA

GROQ_API_KEY = os.getenv("GROQ_API")

### FAZENDO LOGIN
client = Groq(
    api_key=GROQ_API_KEY
)
###PEGANDO CONTEXTO
with open(str(Path("dados/contexto.txt").absolute()), "r") as arquivo:
    context = arquivo.read()


### DEFINIÇÃO PARA ENVIAR O CONTEXTO DE MENSAGENS PARA O BOT
def mensagem_chat(mensagens):
    chat = client.chat.completions.create(
        messages=mensagens,#FORMATO: [{}]
        model="llama3-8b-8192",)
    try:
        resposta = chat.choices[0].message.content
    except:
        resposta = "🤖Estamos enfrentando algum problema..."
    return resposta


def show_page():
    st.pagina_atual="Chat"
    ### INFOS SIDE BAR
    with st.sidebar:
        st.title("💬 Chatbot")
        st.caption("🚀 Tire todas as suas dúvidas sobre a Furia!")
        st.markdown("""<div style='text-align: left; padding: 10px; margin-top: 50px; color: gray;'>
            © 2024 FURIA Esports - Desenvolvido por Edson Carvalho Inturia
        </div>
        """, unsafe_allow_html=True)
        

    ### ANALISANDO SE NA SESSÃO ATUAL O USUÁRIO JÁ ACESSOU O CHAT
    if "chat" not in st.session_state:
        st.session_state["chat"] = [{"role": "assistant", "content": "Olá! Em que posso?"}]

    ### VENDO SE O USUÁRIO DIGITOU ALGO
    if prompt := st.chat_input():
        st.session_state.chat.append({"role": "user", "content": prompt})#INCLUI A MSG DO USUARIO NA VARIAVEL
        mensagens = [{"role": "user","content": context,}] + st.session_state.chat#ADICIONAO CONTEXTO JUNTO COM AS MSGS
        resposta = mensagem_chat(mensagens)#PEGA A RESPOSTA DO BOT
        st.session_state.chat.append({"role":"assistant", "content":resposta})#INCLUI A RESPOSTA NA VARIVEL
    ### EXIBINDO AS MENSAGENS NA TELA
    for msg in st.session_state.chat:
        st.chat_message(msg["role"]).write(msg["content"])
        
