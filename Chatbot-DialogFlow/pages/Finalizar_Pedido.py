import streamlit as st
from secrets import token_hex

# Configuração da página
st.set_page_config(page_title="Pagamento", page_icon="💳", layout="centered", initial_sidebar_state="collapsed")


# Título da página
st.markdown("<h1 style='text-align: center;'>💳 Pagamento</h1>", unsafe_allow_html=True)
st.markdown("---")

# Seção de Resumo do Pedido
if st.session_state.get("pedido"):
    valor_total = 0
    st.markdown("### Resumo do Pedido")
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
            valor_total += item["valor"]
            st.markdown("---")
    st.write(f" \n### Valor Total: {valor_total}")
    st.markdown("---")

    # Opções de Métodos de Pagamento
    st.markdown("### Escolha o Método de Pagamento")
    metodo_pagamento = st.selectbox(
        "Selecione uma opção:",
        ["Cartão de Crédito", "Cartão de Débito", "PIX", "Dinheiro"]
    )

    # Campos Condicionais para Cartão
    if metodo_pagamento in ["Cartão de Crédito", "Cartão de Débito"]:
        st.markdown("#### Informações do Cartão")
        num_cartao = st.text_input("Número do Cartão", max_chars=16, placeholder="XXXX XXXX XXXX XXXX")
        nome_cartao = st.text_input("Nome no Cartão", placeholder="Nome completo")
        validade_cartao = st.text_input("Validade", placeholder="MM/AA")
        cvv = st.text_input("CVV", max_chars=3, type="password", placeholder="***")

    # PIX QR Code
    elif metodo_pagamento == "PIX":
        st.markdown("#### Pague com PIX")
        st.image("https://thumbs.dreamstime.com/b/qr-code-heart-18139677.jpg", width=150, caption="Escaneie o QR Code para pagar")
        st.write(f"Copia e Cola do PIX: `{token_hex(8)}.GOV.PIX0114`")

    # Dinheiro - Troco
    if metodo_pagamento == "Dinheiro":
        valor_dinheiro = st.number_input("Insira o valor pago em dinheiro", min_value=valor_total)
        if valor_dinheiro:
            troco = valor_dinheiro - valor_total
            st.write(f"**Troco**: {troco}")

    # Confirmação e Finalização do Pedido
    st.markdown("---")
    if st.button("Finalizar Pedido"):
        # Validar pagamento (apenas exemplo, adaptável)
        if metodo_pagamento in ["Cartão de Crédito", "Cartão de Débito"] and (not num_cartao or not nome_cartao or not validade_cartao or not cvv):
            st.error("Por favor, preencha todas as informações do cartão.")
        else:
            st.success("Pagamento realizado com sucesso! Seu pedido está sendo preparado.")
            st.balloons()
else:
    st.markdown("---")
    st.markdown("Você precisa fazer um pedido primeiro")
    voltar = st.button("Voltar para o Chat")
    if voltar:
        st.switch_page("app.py")
