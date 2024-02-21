import streamlit as st
import mysql.connector

# Função para conectar ao banco de dados MySQL
connect = mysql.connector.connect(
            host="localhost", #Trocar o host para a sua
            user="root", #Trocar o user para o seu, ou pode deixar o root
            password="123456", #Trocar a senha para a sua
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
        st.write(data)
    elif view == "Ingredients":
        st.write("Aqui estão os ingredientes cadastrados no banco de dados:")
        data = consulta_ingredients(connect)
        st.write(data)
    elif view == "RecipeIngredients":
        st.write("Aqui estão os ingredientes das receitas cadastrados no banco de dados:")
        data = consulta_recipeingredients(connect)
    
    if st.button("Visualizar os dados"):
        if data:
            st.subheader("Consulta:")
            st.dataframe(data)
        else:
            st.write("Nenhum dado encontrado.")

cursor.close()
connect.close()
