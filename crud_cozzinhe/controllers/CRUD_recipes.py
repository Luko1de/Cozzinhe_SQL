import conectar_com_banco as db
import streamlit as st
import pandas as pd
import mysql.connector

def adicionar_receita(recipe):
    try:
        cmd_cre = (f""" INSERT INTO recipes (id_recipes, nome, tags, descricao, quantity)
                    VALUES ('{recipe.id_recipes}', '{recipe.nome}', '{recipe.tags}', '{recipe.descricao}', '{recipe.quantity}')""")
        db.cursor.execute(cmd_cre)
        db.conexao.commit()
    except mysql.connector.IntegrityError as err:
        st.error("Erro ao inserir dados: ", err)
    
def ler_receita():
    cmd_read = (f"""SELECT * FROM recipes""")
    db.cursor.execute(cmd_read)
    resultado = pd.DataFrame(db.cursor.fetchall(), columns=['id_recipes', 'nome', 'tags', 'descricao', 'quantity'])
    st.table(resultado)

def atualizar_receita(recipe):
    cmd_upd = (f"""UPDATE recipes SET nome = '{recipe.nome}', tags = '{recipe.tags}', descricao = '{recipe.descricao}', quantity = '{recipe.quantity}' WHERE id_recipes = '{recipe.id_recipes}'""")
    db.cursor.execute(cmd_upd)
    db.conexao.commit()

def deletar_receita(recipe):
    cmd_del = (f"""DELETE FROM recipes WHERE id_recipes = '{recipe.id_recipes}'""")
    db.cursor.execute(cmd_del)
    db.conexao.commit()
