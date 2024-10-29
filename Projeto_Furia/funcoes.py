import streamlit as st
import pandas as pd
import requests
import os
from pathlib import Path
from datetime import datetime


@st.cache_data
def carregar_dados(dataframe):
    df = pd.read_excel(Path("Projeto_Furia", f"dados/{dataframe}"))
    df = df.set_index("id")
    return df

@st.cache_data
def carregar_ranking(dataframe):
    df = pd.read_excel(Path("Projeto_Furia", f"dados/{dataframe}"))
    return df

@st.cache_data
def carregar_noticias(pesquisa:str):
    API_KEY = {"X-Api-Key": os.getenv("NEWS_API")}
    link = f"https://newsapi.org/v2/everything?q={pesquisa}&sortBy=popularity&language=pt&apiKey={API_KEY["X-Api-Key"]}"
    requisicao = requests.get(link)

    if requisicao.ok:
        requisicao_dict = requisicao.json()
        for noticia in requisicao_dict["articles"]:
            if "furia" in noticia.get("content").lower() or "furia" in noticia.get("description").lower() or pesquisa in noticia.get("content").lower() or pesquisa in noticia.get("description").lower() or "esports" in noticia.get("description").lower():
                with st.sidebar.expander(noticia["title"], expanded=False):
                    st.write(f"```{datetime.strptime(noticia["publishedAt"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")}```")
                    st.markdown(noticia["description"][:130]+"...", help=noticia["description"])
                    st.markdown(f"[Leia mais]({noticia["url"]})", unsafe_allow_html=True)
    else:
        with st.sidebar:
            st.markdown("Sem noticias no momento...")