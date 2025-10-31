from fastapi import FastAPI
import funcao

#Como executar o fastapi
# python -m uvicorn main:app --reload

app = FastAPI(title="Gerenciador de filmes")

#Criando uma rota
@app.get("/")
def home():
    return { "mensagem": "Bem-vindo ao gerenciador de filmes"}

@app.post("/filmes")
def criar_filme(titulo: str, genero: str, ano: int, nota: float):
    funcao.cadastrar_filme(titulo, genero, ano, nota)
    return {"mensagem": "Filme cadastrado com sucesso!"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filmes()
    lista = []
    for linha in filmes:
        lista.append(
            {
                "id": linha[0],
                "titulo": linha[1],
                "genero": linha [2],
                "ano": linha[3],
                "nota": linha[4]
            }
        )
    return {"filmes": lista}

@app.delete("/filmes/{id_filme}")
def deletar_filmes(id_filme: int):
    filmes = funcao.buscar_filmes(id_filme)
    if filmes:
        funcao.deletar_filmes(id_filme)
        return {"mensagem": "Filme excluido com sucesso!"}
    else:
        return{"erro": "Filme não encontrado"}


@app.atualizar("/filme/id_filme")
def atualizar_filmes(id_filme: int, request: request):
    dados = request.json ()
    titulo = dados.get("titulo")
    genero = dados.get("genero")
    ano = dados.get("ano")
    nota = dados.get("nota")

    filmes_existente = funcao.buscar_filme(id_filme)

    if filmes_existente:
        funcao.atualizar_filmes(id_filme, titulo, genero, ano, nota)
        return {"mensagem": "filme atualizado com sucesso!"}
    else:
        return {"erro": "Filme não encontrado"}
