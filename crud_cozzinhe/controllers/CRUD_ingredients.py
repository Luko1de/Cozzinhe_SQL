import conectar_com_banco as db
import streamlit as st
import pandas as pd
import mysql.connector

def adicionar_ingrediente(ingredient):
    try:
        cmd_cre = (f"""INSERT INTO ingredients (id_ingredients, nome)
                        VALUES ('{ingredient.id_ingredients}', '{ingredient.nome}')""")
        db.cursor.execute(cmd_cre)
        db.conexao.commit()
    except mysql.connector.integrityerror as err:
        st.error("Erro ao inserir dados: ", err)
    
def ler_ingrediente():
    cmd_read = (f"""SELECT * FROM ingredients""")
    db.cursor.execute(cmd_read)
    resultado = pd.DataFrame(db.cursor.fetchall(), columns=['id_ingredients', 'nome'])
    st.table(resultado)

def atualizar_ingrediente(ingredient):
    cmd_upd = (f"""UPDATE ingredients SET nome = '{ingredient.nome}' WHERE id_ingredients = '{ingredient.id_ingredients}'""")
    db.cursor.execute(cmd_upd)
    db.conexao.commit()

def deletar_ingrediente(ingredient):
    cmd_del = (f"""DELETE FROM ingredients WHERE id_ingredients = '{ingredient.id_ingredients}'""")
    db.cursor.execute(cmd_del)
    db.conexao.commit()
