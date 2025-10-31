# pip install streamlit requests
import streamlit as st
import requests

#rodae o streamlit
# python -m streamlit run app.py

#URL da API Fastapi
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Filmes", layout="wide")
st.title("Gerenciador de filmes")

menu = st.sidebar.radio("Menu", 
    ["Catalogo de Filmes", "Cadastrar Filmes", "Deletar Filmes"]
    )
if menu == "Catalogo de Filmes":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            st.dataframe(filmes)
        else:
            st.info("Nenhum filme cadastrado ainda!")
    else:
        st.error("Erro ao conectar com a API. ")
elif menu == "Cadastrar Filmes":
    st.subheader("➕ Adicionar filmes")
    titulo = st.text_input("Título do filme")
    genero = st.text_input("Gênero do filme")
    ano = st.number_input("Ano de lançamento", min_value=1900, max_value=2100, step=1)
    nota = st.number_input("Nota (0 a 10)", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Salvar filme: "):
        dados = {"titulo": titulo, "genero": genero, "ano": ano, "nota": nota }
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar filme.")

elif menu == "Deletar Filmes":
    st.subheader("🗑 Deletar Filmes")
    id_filme = st.number_input("Id do filme a excluir", min_value=1, step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/filmes/{id_filme}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Filme excluido com sucesso!!")
            else:
                st.error("Erro ao tentar excluir filme")
        else:
            st.error("Erro ao tentar excluir o filme ")


