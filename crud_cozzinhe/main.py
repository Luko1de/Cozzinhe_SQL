import streamlit as st
import mysql.connector
import pandas as pd
import pages.recipes as recipes
import pages.ingredients as ingredients

# Configurações
st.set_page_config(page_title='CoZZinhe', page_icon=':fork_and_knife:', layout='centered')


with open('C:/Users/lucas/OneDrive/Área de Trabalho/-/Iaad/crud_cozzinhe/data/Cozzinhe_Data.csv') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('CoZZinhe')
st.sidebar.title(':page_facing_up: Menu')
selected = st.sidebar.selectbox('Escolha uma opção', ['Ingredientes', 'Ingredientes'])

if selected == 'Receitas':
    recipes.tela_receitas()

if selected == 'Ingredientes':
    ingredients.tela_ingredients()