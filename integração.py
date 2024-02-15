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
        for indice, linha in dados.iterrows():
            valores = tuple(linha)
            consulta = f"INSERT INTO {tabela} VALUES {valores}"
            cursor.execute(consulta)
        conexao.commit()
        print("Dados inseridos com sucesso na tabela", tabela)
    except mysql.connector.Error as erro:
        print("Erro ao inserir dados no banco de dados MySQL:", erro)

# Leitura do arquivo CSV
df = pd.read_csv("caminho/do/seu/arquivo.csv")

# Seleção aleatória de 20 linhas
dados_aleatorios = df.sample(n=20)

# Chamada da função para conectar ao banco de dados
conexao = conectar_bd()

# Verifica se a conexão foi bem-sucedida
if conexao:
    # Chamada da função para inserir dados no banco de dados
    inserir_dados(conexao, dados_aleatorios, "nome_da_tabela")
