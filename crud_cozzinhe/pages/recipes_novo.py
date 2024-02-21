import streamlit as st
import pandas as pd
import models.recipes as rec
import controllers.CRUD_recipes as crud

def aba_receitas():
    escolha = st.selectbox("Escolha uma opção", ["Create", "Read", "Update", "Delete"])

    if escolha == 'Create':
        st.subheader("Adicionar Receita")
        nome = st.text_input("Nome da receita")
        tags = st.text_input("Tags")
        descricao = st.text_area("Descrição")
        quantity = st.text_input("Quantidade")
        
        st.button("Adicionar")
        recipe = rec.Recipe(nome, tags, descricao, quantity)
        crud.adicionar_receita(recipe)
        st.success("Receita adicionada com sucesso")
    
    elif escolha == 'Read':
        st.subheader("Lista de Receitas")
        crud.ler_receita()
    
    elif escolha == 'Update':
        st.subheader("Atualizar Receita")
        resultado = crud.atualizar_receita()
        resultado = resultado.set_index('id_recipes', 'nome')
    
    elif escolha == 'Delete':
        st.subheader("Deletar Receita")
        resultado = crud.deletar_receita()
        resultado = resultado.set_index('id_recipes', 'nome')