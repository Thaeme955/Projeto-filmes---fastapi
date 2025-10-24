#pip install fastapi uvicorn 
#pip install mysql-connector-python 
#pip install dotenv

import mysql.connector
from dotenv import load_dotenv
import os 

#Carregar .env 
load_dotenv()

def conector():
    try:
        conexao = mysql.connector.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        print("Conexao estabelecida")
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexao: {erro}")
        return None, None

conector()