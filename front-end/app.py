# pip install streamlit requests
import streamlit as st
import requests

#rodae o streamlit
# python -m streamlit run app.py

#URL da API Fastapi
API_URL = "http://127.0.0.1:8000"

st.title("Gerenciador de filmes")

menu = st.sidebar.radio("Menu", 
    ["Catalogo de Filmes", "Cadastrar Filmes"]
    )
if menu == "Catalogo de Filmes":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        st.write("Deu certo!")
        filmes = response.json().get("filmes", [])
    else:
        st.error("Erro ao conectar com a API. ")
