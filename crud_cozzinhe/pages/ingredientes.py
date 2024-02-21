import streamlit as st
import mysql.connector
import pandas as pd
from main import senha
def conectar_bd(senha):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password=senha,
            database="Cozzinhe"
        )
        return conexao
    except mysql.connector.Error as erro:
        st.write("Erro ao conectar ao banco de dados MySQL:", erro)
        return None

def adicionar_ingrediente(conexao, id_ingredients, nome):
    try:
        cursor = conexao.cursor()
        consulta = ("INSERT INTO ingredients (id_ingredients, nome) VALUES (%s, %s)")
        valores = (id_ingredients, nome)
        cursor.execute(consulta, valores)
        conexao.commit()
        st.write('Ingrediente adicionado com sucesso')
    except mysql.connector.Error as erro:
        if erro.errno == 1644:  # Verifica se o erro é específico para violação de unicidade
            st.error('Não é permitido adicionar um ingrediente com o mesmo nome.')
        else:
            st.error(f"Erro ao adicionar ingrediente no banco de dados MySQL: {erro}")


def editar_ingrediente(conexao, id_ingredients, nome):
    try:
        cursor = conexao.cursor()
        consulta = ("UPDATE ingredients SET nome = %s WHERE id_ingredients = %s")
        valores = (nome, id_ingredients)
        cursor.execute(consulta, valores)
        conexao.commit()
        st.write('Ingrediente editado com sucesso')
    except mysql.connector.Error as erro:
        st.write("Erro ao editar ingrediente no banco de dados MySQL:", erro)

def excluir_ingrediente(conexao, id_ingredients):
    try:
        cursor = conexao.cursor()

        # Excluir todas as entradas relacionadas na tabela recipesingredients
        consulta_delete_ri = ("DELETE FROM recipeingredients WHERE id_ingredients = %s")
        cursor.execute(consulta_delete_ri, (id_ingredients,))

        # Excluir o ingrediente na tabela ingredients
        consulta_delete_ingredient = ("DELETE FROM ingredients WHERE id_ingredients = %s")
        cursor.execute(consulta_delete_ingredient, (id_ingredients,))

        conexao.commit()
        st.write('Ingrediente excluído com sucesso')
    except mysql.connector.Error as erro:
        st.write("Erro ao excluir ingrediente no banco de dados MySQL:", erro)


def visualizar_ingrediente(conexao, id_ingredients):
    try:
        cursor = conexao.cursor()
        consulta = ("SELECT * FROM ingredients WHERE id_ingredients = %s")
        cursor.execute(consulta, (id_ingredients,))
        ingrediente = cursor.fetchone()

        if ingrediente:
            st.subheader('Ingrediente Encontrado:')
            st.write(f"ID: {ingrediente[0]}")
            st.write(f"Nome: {ingrediente[1]}")
        else:
            st.warning('Nenhum ingrediente encontrado com o ID fornecido')
    except mysql.connector.Error as erro:
        st.write("Erro ao visualizar ingrediente no banco de dados MySQL:", erro)


conexao = conectar_bd(senha)


def tela_ingredients():
    st.title(':lemon: Ingredientes')
    selected = st.selectbox('Escolha uma ação', ['Adicionar', 'Editar', 'Excluir', 'Visualizar'])

    if selected == 'Adicionar':
        st.subheader('Adicionar ingrediente')
        col1, buff, col2 = st.columns([2,1,2])
        with col1:
            id_ingredients = st.text_input('ID do ingrediente')
        with col2:
            nome = st.text_input('Nome do ingrediente')
        if st.button('Adicionar'):
            adicionar_ingrediente(conexao, id_ingredients, nome)

    if selected == 'Editar':
        st.subheader('Editar ingrediente')
        id_ingredients = st.text_input('ID do ingrediente a ser editado')
        if id_ingredients:
            id_ingredients = int(id_ingredients)
            nome = st.text_input('Nome do ingrediente')
            if st.button('Editar'):
                editar_ingrediente(conexao, id_ingredients, nome)
        else:
            st.warning('Por favor, insira o ID do ingrediente que deseja editar')

    if selected == 'Excluir':
        st.subheader('Excluir ingrediente')
        id_ingredients = st.text_input('ID do ingrediente a ser excluído')
        if id_ingredients:
            id_ingredients = int(id_ingredients)
            if st.button('Excluir'):
                excluir_ingrediente(conexao, id_ingredients)
        else:
            st.warning('Por favor, insira o ID do ingrediente que deseja excluir')

    if selected == 'Visualizar':
        st.subheader('Visualizar ingrediente')
        id_ingredients = st.text_input('ID do ingrediente a ser visualizado')
        if id_ingredients:
            id_ingredients = int(id_ingredients)
            if st.button('Visualizar'):
                read(conexao, id_ingredients)
        else:
            st.warning('Por favor, insira o ID do ingrediente que deseja visualizar')
if conexao:
    tela_ingredients()