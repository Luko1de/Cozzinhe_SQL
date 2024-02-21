import streamlit as st 
import mysql.connector


def adicionar():
    st.title('Adicionar Ingrediente')
    id = st.text_input('ID do Ingrediente')
    nome = st.text_input('Nome do Ingrediente')

    # conectando ao banco de dados e inserindo os dados
    if st.button('Adicionar'):
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="Cozzinhe"
            )
        conexao.cursor().execute(f"INSERT INTO ingredientes (id, nome) VALUES ('{id}', '{nome}')")
        conexao.commit()

