import streamlit as st
import mysql.connector
import pandas as pd

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="Cozzinhe"
        )
        print("Conexão bem-sucedida ao banco de dados MySQL")
        return conexao
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco de dados MySQL:", erro)
        return None

# Função para inserir dados no banco de dados MySQL
def inserir_dados(conexao, dados, tabela):
    try:
        cursor = conexao.cursor()
        colunas = ', '.join(dados.columns)
        for indice, linha in dados.iterrows():
            valores = tuple(linha)
            consulta = f"INSERT INTO {tabela} ({colunas}) VALUES ({', '.join(['%s'] * len(linha))})"
            cursor.execute(consulta, valores)
        conexao.commit()
        print("Dados inseridos com sucesso na tabela", tabela)
    except mysql.connector.Error as erro:
        print("Erro ao inserir dados no banco de dados MySQL:", erro) 

# Leitura do arquivo CSV
# Leitura do arquivo CSV incluindo apenas as colunas desejadas
colunas_desejadas = ['id', 'name', 'tags', 'nutrition', 'ingredients', 'n_ingredients']
df = pd.read_csv("C:/Users/lucas/OneDrive/Área de Trabalho/-/Iaad/Cozzinhe/Cozzinhe_Data.csv", usecols=colunas_desejadas)

# Seleção aleatória de 20 linhas
dados_aleatorios = df.sample(n=20)

# Chamada da função para conectar ao banco de dados
conexao = conectar_bd()

# Verifica se a conexão foi bem-sucedida
if conexao:
    # Chamada da função para inserir dados no banco de dados
    inserir_dados(conexao, dados_aleatorios, "cozzinhe_import")

    # Exibição dos dados na interface web em Streamlit
    st.write("Dados inseridos na tabela:")
    st.dataframe(dados_aleatorios)
