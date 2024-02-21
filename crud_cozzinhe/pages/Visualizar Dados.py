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

# Função para ler os dados do MySQL e retornar um DataFrame
def read_mysql_table(consulta, senha):
    connect = connect_mysql(senha)
    df = pd.read_sql_query(consulta, connect)
    connect.close()
    return df

#Streamlit do READ
st.title(":book: Cozzinhe - Read")
st.write("Aqui você pode visualizar as receitas e ingredientes cadastrados no banco de dados.")

with st.expander("Receitas"):
    st.write("Escolha o que você quer consultar:")
    view = st.selectbox("Escolha a tabela que deseja visualizar:", ["Recipes","Ingredients","RecipeIngredients"])
    if view == "Recipes":
        st.write("Aqui estão as receitas cadastradas no banco de dados:")
        df = read_mysql_table("SELECT id_recipes, nome, tags, descricao, quantity FROM recipes",senha)
        st.table(df)
    elif view == "Ingredients":
        st.write("Aqui estão os ingredientes cadastrados no banco de dados:")
        df = read_mysql_table("SELECT id_ingredients, nome FROM ingredients",senha)
        st.table(df)
    elif view == "RecipeIngredients":
        st.write("Aqui estão os ingredientes das receitas cadastrados no banco de dados:")
        consulta = ("SELECT Recipes.nome AS Nome_Receita, Ingredients.nome AS Nome_Ingrediente "
                    "FROM RecipeIngredients "
                    "JOIN Recipes ON RecipeIngredients.id_recipes = Recipes.id_recipes "
                    "JOIN Ingredients ON RecipeIngredients.id_ingredients = Ingredients.id_ingredients",senha)
        df = read_mysql_table(consulta,senha)
        st.table(df)
