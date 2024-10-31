import streamlit as st
import re
from functools import partial
from pathlib import Path

#Excluir item
def excluir(indice):
    del st.session_state.pedido[indice]
    st.sidebar.error("Item Excluido")

# ITENS PEDIDOS
opcoes_pedido = {"Hambúrguer":10, "Sanduíche Natural":15, "Salgado":8, "Opção Vegetariana":15}
opcoes_acompanhamento = {"Batata Frita":5, "Onion Rings":7, "Salada":500, "Nuggets":13}
opcoes_bebida = {"Refrigerante":5, "Suco Natural":4, "Água":200, "Chá Gelado":2}

st.set_page_config(page_title="Pedido Online - Lanchonete", page_icon="🍔", layout="wide")

# Cabeçalho
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>Pedido Online 🍔🍟</h1>",
    unsafe_allow_html=True,
)

st.markdown("---")
st.subheader("Escolha seu Pedido")

# 1. Escolha do lanche
lanche = st.selectbox("Escolha um lanche:", list(f"{key} - R${value:.2f}" for key, value in opcoes_pedido.items()))

# 2. Escolha de acompanhamento
acompanhamentos = st.multiselect("Selecione seus acompanhamentos:",list(f"{key} - R${value:.2f}" for key, value in opcoes_acompanhamento.items()))

# 3. Bebida
bebida = st.radio("Escolha uma bebida:", list(f"{key} - R${value}" for key, value in opcoes_bebida.items()))

# 4. Observações
observacoes = st.text_area("Alguma observação para o pedido? (Ex: Sem cebola, pão sem glúten...)")

# 5. Quantidade
quantidade = st.number_input("Quantidade:", min_value=1, value=1)

# Incluindo Itens no Carrinho
if st.button("Adicionar ao Carrinho"):
    item = {
        "lanche": lanche[:lanche.index(" -")],
        "acompanhamento": ", ".join([acompanhamento[:acompanhamento.index(" -")] for acompanhamento in acompanhamentos]),
        "bebida": bebida[:bebida.index(" -")],
        "observacoes": observacoes,
        "quantidade": quantidade,
        "valor": 0
    }
    # Incluindo Valor
    for valor in re.findall(r"\d+", lanche + str(acompanhamentos)+ bebida):
        item["valor"] += int(valor)
    else:
        item["valor"] *= int(item["quantidade"])
    st.session_state.pedido.append(item)
    st.success(f"{lanche} adicionado ao carrinho!")

# SideBar
with st.sidebar:
    st.header("🛒 Carrinho")
    # Se houver algum pedido
    if st.session_state.get("pedido"):
        st.subheader("Resumo do Pedido")
    else:
        st.write("Seu carrinho está vazio. Adicione itens para continuar.")
        if st.button("Cancelar", key="cancelar"):
            st.switch_page("app.py")
    

    if 'pedido' not in st.session_state:
        st.session_state.pedido = []

    # Exibe os itens no carrinho
    for i, item in enumerate(st.session_state.pedido, start=1):
        with st.expander(f"**Pedido {i}**:"):
            st.write(f":green[Lanche:] **{item['lanche']}**")
            if item['acompanhamento']:
                st.write(f":green[Acompanhamento(s):] **{item['acompanhamento']}**")
            st.write(f":green[Bebida:] **{item['bebida']}**")
            if item['observacoes']:
                st.info(f"Observações: **{item['observacoes']}**")
            else:
                st.write(":green[Observações:] Sem informações")
            st.write(f":green[Quantidade:] **{item['quantidade']}**")
            st.write(f":green[Valor Total]: R${item["valor"]}")
            st.button("Excluir", key=i, on_click=partial(excluir, i-1), use_container_width=True)
            st.markdown("---")
    if st.session_state.get("pedido"):
        if st.button("Finalizar Pedido"):
            st.session_state.finalizado = True
            st.switch_page("app.py")


st.markdown("<p style='text-align: center; color: gray;'>🍴 Obrigado por escolher nossa lanchonete! 🍴</p>", unsafe_allow_html=True,)
