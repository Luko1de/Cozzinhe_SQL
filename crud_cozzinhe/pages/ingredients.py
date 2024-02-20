import streamlit as st
import controllers.CRUD_ingredients as isingredients
import models.ingredients as ingredients_model

def tela_ingredients():
    st.title('Ingredientes')
    selected = st.selectbox('Escolha uma opção', ['Adicionar', 'Editar', 'Excluir', 'Visualizar'])
    if selected == 'Adicionar':
        isingredients.adicionar()
tela_ingredients()