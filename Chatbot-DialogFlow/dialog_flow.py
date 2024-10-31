from docx import Document
import os
from pathlib import Path
from google.cloud import dialogflow_v2 as dialogflow
import tempfile

# DEFININDO VARIAVEL DE AMBIENTE COM O CAMINHO PARA O ARQUIVO JSON
credentials = os.getenv("DIALOGFLOW_GOOGLE_API")
with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as arquivo_temp:
    arquivo_temp.write(credentials.encode())
    caminho = arquivo_temp.name

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(Path(caminho).absolute())

# ID DO PROJETO PEGO NAS CONFIGURAÇÕES DO DIALOG CONSOLE
PROJECT_ID = os.getenv("PROJECT_ID")

### FUNÇÃO PARA RECOLHER AS PERGUNTAS DO DOCX
def gerar_perguntas(docx):
    doc = Document(docx)
    perguntas_respostas = {}  
    pergunta_atual = None 

    for paragrafo in doc.paragraphs:### LISTA DE PARAGRAFOS
        pergunta_completa = ""
        for i, linha_edicao in enumerate(paragrafo.runs):### PEGO AS EDIÇÕES DO PARAGRAFO
            if linha_edicao.bold and linha_edicao.underline:### VEJO SE ESTÁ EM NEGRITO E SUBLINHADO
                tamanho = len(paragrafo.runs)### ALGUMAS LINHAS TEM MAIS DE UMA EDIÇÃO ENTÃO EU PEGO O TAMANHO
                if  tamanho > 1:
                    pergunta_completa += linha_edicao.text
                    if tamanho == i+1:
                        pergunta_atual = pergunta_completa
                        perguntas_respostas[pergunta_atual] = []### ADICIONO A PERGUNTA NO DICIONARIO
                elif tamanho == 1:
                    pergunta_atual = linha_edicao.text.strip()
                    perguntas_respostas[pergunta_atual] = []
            elif pergunta_atual:
                perguntas_respostas[pergunta_atual].append(linha_edicao.text.strip()) ### ADICIONO A RESPOSTA NO DICIONARIO
        
    for key in perguntas_respostas:
        perguntas_respostas[key] = " ".join(perguntas_respostas[key])### CORRIJO AS RESPOSTAS
    return perguntas_respostas


### FUNÇÃO PARA ADICIONAR UM INTENT NO DIALOGFLOW(NIVEL: DIFICIL haha)
def adicionar_intent(project_id, nome, perguntas, respostas):
    
    client = dialogflow.IntentsClient()### CRIO UM CLIENTE
    parent = dialogflow.AgentsClient.agent_path(project_id)### PEGO O AGENTE/ATENDENTE ATUAL

    # LISTA DAS PERGUNTAS
    if type(perguntas) == list:
        pergunta_treino = []
        for pergunta in perguntas:
            pergunta_treino.append({"parts": [{"text": pergunta}]})

    else:
        pergunta_treino = [
            {"parts": [{"text": perguntas}]}  
        ]

    # LISTA DAS RESPOSTAS
    resposta_treino = [{"text": {"text": respostas}}]

    # DICIONARIO DO INTENT
    intent = {
        "display_name": nome,
        "training_phrases": pergunta_treino,
        "messages": resposta_treino,
    }

    # { FORMATO DO DICIONARIO PARA VISUALIZAÇÃO
    #     "display_name": nome,
    #     "training_phrases": [{
    #         'parts':[{
    #             'text':"Qual o preço?"
    #         }]
    #     }],
    #     "messages": [{
    #         "text": {"text":["5 reais"]}
    #     }],
    # }

    # CHAMANDO A API PARA CRIAR O INTENT
    api = client.create_intent(request={"parent": parent, "intent": intent})
    print(f"Intent criada: {api.name}")


# Envia uma mensagem para o agente
def enviar_mensagem(credenciais, session_id, mensagem):
    cliente = dialogflow.SessionsClient()
    session = cliente.session_path(credenciais, session_id)

    text_input = dialogflow.types.TextInput(text=mensagem, language_code="pt-BR")
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = cliente.detect_intent(request={"session": session, "query_input": query_input})
    return response.query_result.fulfillment_text

# Incluindo e as peguntas no DialogFlow
if __name__ == "__main__":
    lista_perguntas = gerar_perguntas("Perguntas.docx")
    for key, value in lista_perguntas.items():
        adicionar_intent(project_id=PROJECT_ID, nome=key[:20], perguntas=key.split("|"), respostas=[value])
    

    # perguntas = gerar_perguntas("Perguntas.docx")

    # for key, value in perguntas.items():
    #     adicionar_intent(PROJECT_ID, key[:20], key+"?", value)


# adicionar_intent(project_id=PROJECT_ID, nome="Teste",perguntas=["Quanto custa", "Qual o valor?"],respostas=["5 reais", "100 reais"] )