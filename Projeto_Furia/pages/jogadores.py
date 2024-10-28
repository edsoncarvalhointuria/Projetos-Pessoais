import streamlit as st
import plotly.express as px
from streamlit_navigation_bar import st_navbar
from funcoes import carregar_dados
from PIL import Image


def show_page():
    dados = carregar_dados("dados.xlsx")#PEGANDO INFOS JOGADOS
    ### SEÇÃO COM DADOS PESSOAIS JOGADORES
    sidebar = st.sidebar
    with sidebar:
        st.header("Escolha um jogador")
        escolha = st.selectbox("Selecione um jogador:", list(dados.index))
        

    coluna_esquerda, coluna_direita = st.columns([0.7, 2.5])
    coluna_esquerda.image(f"images/{escolha}.webp") 
    coluna_direita.title(escolha)

    container = coluna_direita.container()
    #MELHORANDO A PLANILHA
    st.markdown("""
    <style>
    table {
        border-collapse: collapse; 
        border: 0; 
        width: 100%;
    }
    th, td {
        border: none;
        text-align: left;
        padding: 5px;
    }
    </style>""", unsafe_allow_html=True)
    with container:
        st.markdown(f"""
        | **Nome:** | <strong>```{dados.loc[escolha, "Nome"]}```</strong> |
        |---|---|
        | **Idade:** | <strong>```{dados.loc[escolha, "Idade"]}```</strong> |
        | **Nacionalidade:** | <strong>```{dados.loc[escolha, "Nacionalidade"]}```</strong> |
        """, unsafe_allow_html=True)
            
    ### VIDEO DO JOGADOR
    st.video(f"videos/{escolha}.mp4")

    ### DESCRIÇÃO DO JOGADOR
    st.write(f"""
    {dados.loc[escolha, "descricao"]}
    <br><br>

    ---""", unsafe_allow_html=True) 

    ### GRAFICO CONQUISTAS E ESTASTISCAS
    st.header("Principais Títulos e Conquistas")

    torneios = carregar_dados("torneios.xlsx")
    torneios = torneios.loc[escolha, :]
    torneios['posicao invertida'] = torneios['posicao'].max() - torneios['posicao'] + 2 #DEIXANDO O 1 COMO MAIOR VALOR


    fig = px.bar(data_frame=torneios, x='torneio', y='posicao invertida', hover_data={"posicao invertida":False,"torneio":True, "posicao":True, "ano":True},
        text='posicao', labels={"posicao invertida": "Colocação 🥇", "posicao": "Colocação 🥇", "torneio": "Torneio 🏆", "ano":"Ano"})

    for i, x in enumerate(torneios["torneio"]):### INCLUINDO AS IMAGENS DOS TORNEIOS NO GRÁFICO
        fig.add_layout_image(source=Image.open("images/campeonatos/"+x+".png"), 
            x=i,y=-0.2,xref="x",yref="y",xanchor="center",sizex=0.5,sizey=0.5,)
    fig.update_layout(xaxis={"visible":False}, yaxis={"range":[-1.5, max(torneios["posicao invertida"])+0.5], "showticklabels":False})
    fig.update_traces(marker_color=["#FFD700" if posicao == 1 else "#C0C0C0" if posicao == 2 else "#CD7F32" for posicao in torneios['posicao']])

    ### DIFININDO DUAS SEÇÕES
    parte1, parte2 = st.tabs(["🏆 Conquistas", "📈 Estatísticas"])


    parte1.plotly_chart(fig)

    ### DEFINDO ESTATISTICAS JOGADORES
    estatisticas = carregar_dados("estatisticas.xlsx")
    div_coluna = ""
    for coluna in estatisticas:# MONTANDO A TABELA
        div_coluna += """
    <div style="text-align: center; color: orange;">
        <h5>{}</h5>
        <p>{}</p>
    </div>""".format(coluna, estatisticas.loc[escolha, coluna])


    parte2.markdown(f"""
    <div style="display: flex; justify-content: center; gap: 15px; background-color: black; padding: 15px; border-radius: 8px;">
        {div_coluna}    
    </div>
    """, unsafe_allow_html=True)

    ### FIM DA PAGINA
    st.markdown("""
    <div style='text-align: center; padding: 10px; margin-top: 50px; color: gray;'>
        © 2024 FURIA Esports - Desenvolvido por Edson Carvalho Inturia
    </div>
    """, unsafe_allow_html=True)