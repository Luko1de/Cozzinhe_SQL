import streamlit as st
import mysql.connector
from main import senha

# Função para conectar ao banco de dados MySQL
def conectar_bd(senha):
    try:
        conexao = mysql.connector.connect(
<<<<<<< HEAD
<<<<<<< HEAD
            host="localhost",
            user="root",
            password=senha,
=======
            host="localhost", #Trocar o host para a sua
            user="root", #Trocar o user para o seu, ou pode deixar o root
            password="123456", #Trocar a senha para a sua
>>>>>>> f5d743c4f4162368cb8e8e71ff9f4489316f0dbd
=======
            host="localhost",
            user="root",
            password="123456",
>>>>>>> b2c19ff92db8278fe1315eaafbbe96d5be4f6ba2
            database="cozzinhe"
        )
        st.write("Conexão bem-sucedida ao banco de dados MySQL")
        return conexao
    except mysql.connector.Error as erro:
        st.write("Erro ao conectar ao banco de dados MySQL:", erro)
        return None

# Função para consultar os ingredientes de uma receita específica
def consultar_ingredientes_por_receita(conexao, id_receita):
    try:
        cursor = conexao.cursor()
        consulta = ("SELECT Recipes.nome, Ingredients.nome "
                    "FROM RecipeIngredients "
                    "JOIN Recipes ON RecipeIngredients.id_recipes = Recipes.id_recipes "
                    "JOIN Ingredients ON RecipeIngredients.id_ingredients = Ingredients.id_ingredients "
                    "WHERE RecipeIngredients.id_recipes = %s")
        cursor.execute(consulta, (id_receita,))
        ingredientes = cursor.fetchall()
        return ingredientes
    except mysql.connector.Error as erro:
        st.write("Erro ao consultar ingredientes no banco de dados MySQL:", erro)

# Interface do Streamlit
st.title("Consulta de Ingredientes por Receita")
id_receita = st.text_input("Insira o ID da receita:")
if st.button("Consultar"):
    conexao = conectar_bd(senha)
    if conexao:
        ingredientes = consultar_ingredientes_por_receita(conexao, id_receita)
        if ingredientes:
            receita_atual = None
            st.subheader("Ingredientes da Receita:")
            for receita, ingrediente in ingredientes:
                if receita != receita_atual:
                    st.write(f"Receita: {receita}")
                    receita_atual = receita
                st.write(f"- Ingrediente: {ingrediente}")
        else:
            st.warning("Nenhum ingrediente encontrado para o ID da receita fornecido.")
        conexao.close()
