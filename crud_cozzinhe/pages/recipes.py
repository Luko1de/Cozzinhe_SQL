import streamlit as st
import mysql.connector  # Importe o módulo MySQL Connector

def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="localhost", #Trocar o host para a sua
            user="root", #Trocar o user para o seu, ou pode deixar o root
            password="123456", #Trocar a senha para a sua
            database="Cozzinhe"
        )
        st.write("Conexão bem-sucedida ao banco de dados MySQL")
        return conexao
    except mysql.connector.Error as erro:
        st.write("Erro ao conectar ao banco de dados MySQL:", erro)
        return None

def adicionar_receita(conexao, id_recipes, nome, tags, descricao, n_ingredientes):
    try:
        cursor = conexao.cursor()
        consulta = ("INSERT INTO recipes (id_recipes, nome, tags, descricao, quantity) VALUES (%s, %s, %s, %s, %s)")
        valores = (id_recipes, nome, tags, descricao, n_ingredientes)
        cursor.execute(consulta, valores)
        conexao.commit()
        st.write('Receita adicionada com sucesso')
    except mysql.connector.Error as erro:
        if erro.errno == 1644:  # Verifica se o erro é específico para violação de unicidade
            st.error('Não é permitido adicionar uma receita com o mesmo nome.')
        else:
            st.error(f"Erro ao adicionar receita no banco de dados MySQL: {erro}")


def editar_receita(conexao, id_recipes, nome, tags, descricao, n_ingredientes):
    try:
        cursor = conexao.cursor()
        consulta = ("UPDATE recipes SET nome = %s, tags = %s, descricao = %s, quantity = %s WHERE id_recipes = %s")
        valores = (nome, tags, descricao, n_ingredientes, id_recipes)
        cursor.execute(consulta, valores)
        conexao.commit()
        st.write('Receita editada com sucesso')
    except mysql.connector.Error as erro:
        st.write("Erro ao editar receita no banco de dados MySQL:", erro)

def excluir_receita(conexao, id_recipes):
    try:
        cursor = conexao.cursor()

        # Excluir todas as entradas relacionadas na tabela recipesingredients
        consulta_delete_ri = ("DELETE FROM recipeingredients WHERE id_recipes = %s")
        cursor.execute(consulta_delete_ri, (id_recipes,))

        # Excluir a receita na tabela recipes
        consulta_delete_recipe = ("DELETE FROM recipes WHERE id_recipes = %s")
        cursor.execute(consulta_delete_recipe, (id_recipes,))

        conexao.commit()
        st.write('Receita excluída com sucesso')
    except mysql.connector.Error as erro:
        st.write("Erro ao excluir receita no banco de dados MySQL:", erro)


def visualizar_receita(conexao, id_recipes):
    try:
        cursor = conexao.cursor()
        consulta = ("SELECT * FROM recipes WHERE id_recipes = %s")
        cursor.execute(consulta, (id_recipes,))
        receita = cursor.fetchone()

        if receita:
            st.subheader('Receita Encontrada:')
            st.write(f"ID: {receita[0]}")
            st.write(f"Nome: {receita[1]}")
            st.write(f"Tags: {receita[2]}")
            st.write(f"Descrição: {receita[3]}")
            st.write(f"Quantidade de ingredientes: {receita[4]}")
        else:
            st.warning('Nenhuma receita encontrada com o ID fornecido')
    except mysql.connector.Error as erro:
        st.write("Erro ao visualizar receita no banco de dados MySQL:", erro)

conexao = conectar_bd()
def tela_receitas():
     # título com ícone de panela
    st.title(':fork_and_knife: Receitas')
    # selecionar ação CRUD - Adicionar
    selected = st.selectbox('Escolha uma ação', ['Adicionar', 'Editar', 'Excluir', 'Visualizar'])
    show = st.checkbox('Mostrar receitas')

    # se ação for Adicionar
    if selected == 'Adicionar':
        # formulário para adicionar receita
        st.subheader('Adicionar receita')
        id_recipes = st.text_input('ID da receita')
        nome = st.text_input('Nome da receita')
        tags = st.text_input('Tags')
        descricao = st.text_area('Descrição')
        n_ingredientes = st.number_input('Número de ingredientes', min_value=1, max_value=100)
        # botão para adicionar receita
        if st.button('Adicionar'):
            adicionar_receita(conexao, id_recipes, nome, tags, descricao, n_ingredientes)
    if selected == 'Editar':
        # formulário para editar receita
        st.subheader('Editar receita')
        id_recipes = st.text_input('ID da receita a ser editada')
        if id_recipes:  # Verifica se o ID da receita foi inserido
            id_recipes = int(id_recipes)  # Convertendo para inteiro
            nome = st.text_input('Nome da receita')
            tags = st.text_input('Tags')
            descricao = st.text_area('Descrição')
            n_ingredientes = st.number_input('Número de ingredientes', min_value=1, max_value=100)
            # botão para editar receita
            if st.button('Editar'):
                editar_receita(conexao, id_recipes, nome, tags, descricao, n_ingredientes)
        else:
            st.warning('Por favor, insira o ID da receita que deseja editar')



    # se ação for Excluir
    if selected == 'Excluir':
        # formulário para excluir receita
        st.subheader('Excluir receita')
        id_recipes = st.text_input('ID da receita a ser excluída')
        if id_recipes:  # Verifica se o ID da receita foi inserido
            id_recipes = int(id_recipes)  # Convertendo para inteiro
            # botão para excluir receita
            if st.button('Excluir'):
                excluir_receita(conexao, id_recipes)
        else:
            st.warning('Por favor, insira o ID da receita que deseja excluir')
    # se ação for Visualizar
    if selected == 'Visualizar':
        # formulário para visualizar receita
        st.subheader('Visualizar receita')
        id_recipes = st.text_input('ID da receita a ser visualizada')
        if id_recipes:  # Verifica se o ID da receita foi inserido
            id_recipes = int(id_recipes)  # Convertendo para inteiro
            # botão para visualizar receita
            if st.button('Visualizar'):
                visualizar_receita(conexao, id_recipes)
        else:
            st.warning('Por favor, insira o ID da receita que deseja visualizar')
tela_receitas()
