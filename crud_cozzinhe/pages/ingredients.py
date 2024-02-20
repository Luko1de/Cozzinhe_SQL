import streamlit as st
import mysql.connector

def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="Cozzinhe"
        )
        st.write("Conexão bem-sucedida ao banco de dados MySQL")
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
        st.write("Erro ao adicionar ingrediente no banco de dados MySQL:", erro)

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
        consulta = ("DELETE FROM ingredients WHERE id_ingredients = %s")
        cursor.execute(consulta, (id_ingredients,))
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

conexao = conectar_bd()


def tela_ingredients():
    st.title(':lemon: Ingredientes')
    selected = st.selectbox('Escolha uma ação', ['Adicionar', 'Editar', 'Excluir', 'Visualizar'])

    if selected == 'Adicionar':
        st.subheader('Adicionar ingrediente')
        id_ingredients = st.text_input('ID do ingrediente')
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
                visualizar_ingrediente(conexao, id_ingredients)
        else:
            st.warning('Por favor, insira o ID do ingrediente que deseja visualizar')
if conexao:
    tela_ingredients()