import streamlit as st
import mysql.connector
<<<<<<< HEAD
from main import senha

# Função para conectar ao banco de dados MySQL
connect = mysql.connector.connect(
<<<<<<< HEAD
            host="127.0.0.1",
            user="root",
            password=senha,
=======
            host="localhost", #Trocar o host para a sua
            user="root", #Trocar o user para o seu, ou pode deixar o root
            password="123456", #Trocar a senha para a sua
>>>>>>> f5d743c4f4162368cb8e8e71ff9f4489316f0dbd
=======
import pandas as pd

# Função para conectar ao banco de dados MySQL
connect = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
>>>>>>> b2c19ff92db8278fe1315eaafbbe96d5be4f6ba2
            database="Cozzinhe"
        )
    
cursor = connect.cursor()

#Consulta das receitas no banco de dados
def consulta_recipes(connect):
    leitura = "SELECT * FROM recipes"
    cursor = connect.cursor()
    cursor.execute(leitura)
    data = cursor.fetchall()
    return data

#Consulta dos ingredientes no banco de dados
def consulta_ingredients(connect):
    leitura = "SELECT * FROM ingredients"
    cursor = connect.cursor()
    cursor.execute(leitura)
    data = cursor.fetchall()
    return data

#Consulta dos ingredientes das receitas no banco de dados
def consulta_recipeingredients(connect):
    leitura = "SELECT * FROM recipeingredients"
    cursor = connect.cursor()
    cursor.execute(leitura)
    data = cursor.fetchall()
    return data

#Streamlit do READ
st.title(":book: Cozzinhe - Read")
st.write("Aqui você pode visualizar as receitas e ingredientes cadastrados no banco de dados.")
with st.expander("Receitas"):
    st.write("Escolha o que você quer consultar:")
    view = st.selectbox("Escolha a tabela que deseja visualizar:", ["Recipes","Ingredients","RecipeIngredients"])
    if view == "Recipes":
        st.write("Aqui estão as receitas cadastradas no banco de dados:")
        data = consulta_recipes(connect)
        if st.button("Visualizar os dados"):
            if data:
                st.subheader("Consulta:")
                st.dataframe(data)
            else:
                st.write("Nenhum dado encontrado.")
    elif view == "Ingredients":
        st.write("Aqui estão os ingredientes cadastrados no banco de dados:")
        data = consulta_ingredients(connect)
        if st.button("Visualizar os dados"):
            if data:
                st.subheader("Consulta:")
                st.dataframe(data)
            else:
                st.write("Nenhum dado encontrado.")
    elif view == "RecipeIngredients":
        # Consulta para selecionar todas as receitas e seus ingredientes
        consulta = ("SELECT Recipes.nome AS Nome_Receita, Ingredients.nome AS Nome_Ingrediente "
                    "FROM RecipeIngredients "
                    "JOIN Recipes ON RecipeIngredients.id_recipes = Recipes.id_recipes "
                    "JOIN Ingredients ON RecipeIngredients.id_ingredients = Ingredients.id_ingredients")
        cursor.execute(consulta)
        data = cursor.fetchall()
        
        if st.button("Visualizar os dados"):
            if data:
                st.subheader("Consulta:")
                st.dataframe(data)
            else:
                st.write("Nenhum dado encontrado.")

cursor.close()
connect.close()

