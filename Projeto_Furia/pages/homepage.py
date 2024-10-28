import streamlit as st
import re
from funcoes import carregar_ranking
import plotly.express as px
from pathlib import Path
from funcoes import carregar_noticias
from streamlit_carousel import carousel
from streamlit_javascript import st_javascript
from user_agents import parse
from PIL import Image



def show_page():
   
   ### COLANDO O FUNDO DA HOMEPAGE
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.7)), url('https://byluan.co/wp-content/uploads/2023/05/1.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }
    .button-container {
            margin-top: 20px;
            margin-bottom: 20px;
    }
    .cta-button {
        background-color: #7bd192;
        border: none;
        padding: 10px 20px;
        font-size: 1rem;
        border-radius: 5px;
        cursor: pointer;
        margin: 2px;
    }
    .cta-button:hover {
        background-color: #5aa872;
    }""",unsafe_allow_html=True)

    ### ALTERANDO O ESPAÇAMENTO DA NOTICIAS
    st.markdown("""
    <style>
        .st-emotion-cache-8atqhb {
        margin-top: -50px;
        }
    </style>""", unsafe_allow_html=True)
    st.sidebar.markdown("## 📢 Últimas Notícias")
    carregar_noticias("furia")

    ### INICIO DA PAGINA
    st.html(f"""
    <div style='text-align: center;'>
        <h1 style='color:#619DED'>FURIA Esports - CS2</h2>
        <p>FUTURO EM JOGO: Estágio de verão da Cruzeiro do Sul.<p>
        <div class='button-container' style='padding:10px'>
            <a href='https://www.instagram.com/furiagg' style='color:white; text-decoration: none;' class='cta-button'>Siga a Furia</a>
            <a href="https://www.99jobs.com/furia/jobs/398294-estagio-de-verao-cruzeiro-do-sul-tech-engenharia-de-software" style='color:white; text-decoration: none;' class='cta-button'>Junte-se à FURIA</a>
        </div>
    </div>
    <br>
    """)
    ### IMAGEM CENTRAL
    st.image(Image.open('Projeto_Furia/images/equipe.png'), 'Elisa Masters Espoo 2023', use_column_width=True)

    ### BREVE DESCRIÇÃO SOBRE A FURIA
    st.header("Sobre a Furia")
    st.write("""
    A FURIA Esports é uma das principais organizações de esportes eletrônicos do Brasil. Fundada em 2017, a equipe se destaca não apenas por sua habilidade e conquistas no cenário competitivo, mas também pelo seu compromisso com inovação, paixão e crescimento sustentável.

    Em especial, o time de Counter-Strike da FURIA é reconhecido mundialmente pela sua performance excepcional. Com jogadores lendários como FalleN, KSCERATO, chelo, yuurih e skullz, a equipe continuamente redefine o padrão de excelência no jogo. Cada vitória não é apenas um testemunho de suas habilidades, mas também de sua dedicação incansável e amor pelo jogo.

    A FURIA não é apenas uma equipe, mas uma força inovadora que inspira novos talentos e eleva os esportes eletrônicos a novas alturas.
    <br><br>""", unsafe_allow_html=True)

    ### GRÁFICO COM RANKING DAS POSIÇÕES GLOBAIS DE CS
    ranking = carregar_ranking("ranking_mundial.xlsx")

    fig = px.line(data_frame=ranking, x="Data", y="Posicao", title="Ranking Mundial - CS🌎", labels={"Posicao": "Posição"},
                    hover_data={"Equipe":True}, range_y=[ranking["Posicao"].max()+5, 1])
    
    fig.update_xaxes(title="")#REMOVENDO O LABEL DO X
    fig.update_traces(mode="markers+lines")#INCLUINDO OS MARCADORES NA LINHAS
    fig.update_layout(title_automargin=False, title_font_size=30,title_x=0.03, margin={"pad":20})#ALTERANDO A POSIÇÃO DO TITULO DO GRÁFICO
    st.plotly_chart(fig)

    ### FORMA DE PEGAR INFOS JAVASCRIPT NO STREAMLIT
    ua_string = st_javascript("""window.navigator.userAgent;""")
    user_agent = parse(str(ua_string))

    ### BREVE DESCRIÇÃO SOBRE O TIME DE CS DA FURIA
    st.html("<br>")
    st.markdown("## Nosso Time de CS")
    col1, col2 = st.columns([1, 6])
    with col1:
        if user_agent.is_mobile:
            st.html("""
            <div style="text-align: center;">
                <img src='app/static/cslogo3.png' width='200px'>
            </div>""")
        else:
            st.image("Projeto_Furia/images/cslogo3.png", use_column_width=True, width=200)
    with col2:
        st.write(
            """
            Nossa equipe de **Counter Strike** é composta pelos melhores talentos do cenário brasileiro e mundial.
            Com uma mentalidade vencedora e um espírito de equipe inabalável, continuamos em busca de conquistas 
            em torneios internacionais.
            Essa química única entre nossos jogadores é o que nos torna temidos e respeitados em cada competição que participamos. Veja abaixo algumas fotos dos nossos campeões em ação.
            """)
        st.html("""<br><br>""")

    ### CARROSSEL DE IMAGENS
    fotos = [
        dict(title=re.findall(r"\D+",foto.stem)[0],
            text="",
            img= foto.absolute(),
            link="https://www.instagram.com/furiagg/?hl=pt-br",) for foto in Path("Projeto_Furia","images/Carrossel").iterdir()
    ]
 
    carousel(items=fotos, width=1, container_height=450)

    
    if user_agent.is_mobile:### O CARROSSEL ESTAVA COM UM BUG NO MOBILE, ENTÃO FOI ADICIONADO ESTE IF PARA SOLUÇÃO
        st.html("""
            <style>
                iframe[src*="streamlit_carousel"] {
                    height: auto !important;  
                }
            </style>""")


    ### FIM HOMEPAGE
    st.markdown("""
    <div style='text-align: center; padding: 10px; margin-top: 50px; color: gray;'>
        © 2024 FURIA Esports - Desenvolvido por Edson Carvalho Inturia
    </div>
    """, unsafe_allow_html=True)