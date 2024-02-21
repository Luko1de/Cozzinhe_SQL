import streamlit as st
import mysql.connector
import pandas as pd
from main import senha

# Função para conectar ao banco de dados MySQL
def connect_mysql(senha):
    return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=senha,
            database="Cozzinhe"
        )


#Streamlit do READ
st.title(":book: Cozzinhe - Consultas")
st.write("Aqui você pode visualizar as receitas e ingredientes cadastrados no banco de dados.")
st.divider()
st.subheader("Escolha o que você quer consultar:")
view = st.selectbox("Escolha a tabela que deseja visualizar:", ["Receitas","Ingredientes","Ingredientes de cada Receita"])
if view == "Receitas":
    st.write("Aqui estão as receitas cadastradas no banco de dados:")
    comando = "SELECT * FROM recipes"
    conexao = connect_mysql(senha)
    cursor=conexao.cursor()
    cursor.execute(comando)
    df = pd.DataFrame(cursor.fetchall(), columns=["ID","Nome","Tags","Descrição","Quantidade de Ingredientes"])
    st.table(df)
if view == "Ingredientes":
    st.write("Aqui estão os ingredientes cadastrados no banco de dados:")
    comando = "SELECT * FROM ingredients"
    conexao = connect_mysql(senha)
    cursor=conexao.cursor()
    cursor.execute(comando)
    df = pd.DataFrame(cursor.fetchall(), columns=["ID","Nome"])
    st.table(df)
if view == "Ingredientes de cada Receita":
    st.write("Aqui estão os ingredientes das receitas cadastrados no banco de dados:")
    comando = ("SELECT Recipes.nome AS Nome_Receita, Ingredients.nome AS Nome_Ingrediente "
                    "FROM RecipeIngredients "
                    "JOIN Recipes ON RecipeIngredients.id_recipes = Recipes.id_recipes "
                    "JOIN Ingredients ON RecipeIngredients.id_ingredients = Ingredients.id_ingredients")
    conexao = connect_mysql(senha)
    cursor=conexao.cursor()
    cursor.execute(comando)
    df = pd.DataFrame(cursor.fetchall(), columns=["Receita","Ingrediente"])
    st.table(df)