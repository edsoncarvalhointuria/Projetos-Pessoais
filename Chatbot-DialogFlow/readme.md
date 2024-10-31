
# 🍔 Chatbot de Lanchonete Fake

Esse projeto foi criado para explorar o uso do Dialogflow na criação de um chatbot simples para uma lanchonete fictícia. O chatbot é capaz de responder perguntas comuns sobre o cardápio, tempo de entrega, formas de pagamento, entre outros tópicos básicos, simulando um atendimento amigável e eficiente em uma lanchonete.

> ⚠️ **Observação**: Este projeto é apenas para fins de aprendizado e não tem nenhum propósito comercial.

🔗 **Acesse o site**: [Streamlit.io](https://dialog-flow-bot.streamlit.app/)

---

## 📋 Funcionalidades

- **Interações Simples**: O chatbot responde a perguntas frequentes sobre o cardápio, pedidos, formas de pagamento, e promoções da lanchonete.
- **Opções de Pedido**: Simula o processo de escolha de itens e permite que o usuário veja um "recibo" final ao concluir o pedido.
- **Mensagens Personalizadas**: Oferece respostas automáticas com base nos intents definidos no Dialogflow.
- **Comando para Finalizar**: Após o usuário escolher os itens do pedido, ele pode digitar #FINALIZAR para ir para página de pagamento.
- **Comando para Editar**: Após o usuário escolher os itens do pedido, ele pode digitar #EDITAR para fazer alterações no pedido.

## 🛠️ Tecnologias Utilizadas
- **Dialogflow**: Gerencia os intents e o fluxo de respostas para o chatbot.
- **Python**: A base do código, incluindo lógica de comunicação entre Dialogflow e Streamlit.
- **Streamlit**: Framework para a criação da interface web onde o chatbot é acessado.
- **Pillow**: Biblioteca para manipulação de imagens e geração de recibos.

## 🚀 Como Funciona o Chatbot
1. **Início**: Ao acessar a página, o chatbot dá boas-vindas e exibe as opções iniciais para o usuário interagir.
2. **Intents do Dialogflow**: Cada pergunta ou comando digitado pelo usuário é analisado pelo Dialogflow, que retorna uma resposta configurada.
3. **Finalização do Pedido**: O chatbot registra os itens escolhidos e, ao finalizar, exibe o recibo simulado no chat.
4. **Pagamento**: O chatbot pergunta se o usuário quer finalizar o pedido, se ele responder positivamente, o bot encaminhar ele para a página de pagamento.

## 📄 Exemplo de Interação

**Usuário**: Quais são os lanches do cardápio?

**Chatbot**: Nós temos hambúrgueres, sanduíches naturais, salgados, e opções vegetarianas. Qual você gostaria de saber mais?

---

**Usuário**: Qual o tempo de entrega?

**Chatbot**: O tempo de entrega varia de 30 a 60 minutos.

---

**Usuário**: Quero finalizar o pedido

**Chatbot**: *Quer finalizar o pedido?*

---

## 💌 Quer falar comigo?

Entre em contato:

<p align="left">  
<a href="mailto:edsoncarvalhointuria@gmail.com" title="Gmail">  
  <img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white" alt="Gmail"/>  
</a>  
<a href="#" title="LinkedIn">  
  <img src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/>  
</a>  
</p>

---
