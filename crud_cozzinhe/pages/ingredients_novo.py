import streamlit as st
import pandas as pd
import controllers.CRUD_ingredients as crud
import models.ingredients as ing

def aba_ingredientes():
    escolha = st.selectbox("Escolha uma opção", ["Create", "Read", "Update", "Delete"])

    if escolha == 'Create':
        st.subheader("Adicionar Ingrediente")
        nome = st.text_input("Nome do ingrediente")
        
        st.button("Adicionar")
        ingredient = ing.Ingredient(nome)
        crud.adicionar_ingrediente(ingredient)
        st.success("Ingrediente adicionado com sucesso")
    
    elif escolha == 'Read':
        st.subheader("Lista de Ingredientes")
        crud.ler_ingrediente()
    
    elif escolha == 'Update':
        st.subheader("Atualizar Ingrediente")
        resultado = crud.atualizar_ingrediente()
        resultado = resultado.set_index('id_ingredients', 'nome')
    
    elif escolha == 'Delete':
        st.subheader("Deletar Ingrediente")
        resultado = crud.deletar_ingrediente()
        resultado = resultado.set_index('id_ingredients', 'nome')
