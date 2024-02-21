import mysql.connector
import streamlit as st
conexao = mysql.connector.connect(
            host="localhost", #Trocar o host para a sua
            user="root", #Trocar o user para o seu, ou pode deixar o root
            password="123456", #Trocar a senha para a sua
            database="Cozzinhe"
        )
cursor = conexao.cursor()
