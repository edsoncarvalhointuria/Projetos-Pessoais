import streamlit as st
from streamlit_navigation_bar import st_navbar
from pages import homepage, jogadores, chat

### PAGINA GERENCIADORA
    #CONFIGURAÇÕES INICIAIS DA PAGINA
st.set_page_config(page_title="FURIA CS:GO", page_icon="Projeto_Furia/images/logo.png", layout="wide", initial_sidebar_state="expanded")

### CRIANDO UMA VARIAVEL PARA GERENCIAR AS PAGINAS
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"

### CRIANDO NAVBAR 
pages = ["Home", "Jogadores", "Chat"]
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(pages, styles=styles)#PEGA A PAGINA QUE O USUARIO CLICOU

### GERENCIANDO PAGINAS
if page != st.session_state["pagina_atual"]:
    st.session_state.pagina_atual = page
    st.rerun()
    

### EXIBINDO AS PAGINAS
functions = {
    "Home":homepage.show_page,
    "Jogadores":jogadores.show_page,
    "Chat":chat.show_page,
}
functions.get(page)()







