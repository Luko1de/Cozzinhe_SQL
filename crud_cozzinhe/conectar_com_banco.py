<<<<<<< HEAD
import mysql.connector
import streamlit as st
conexao = mysql.connector.connect(
            host="localhost", #Trocar o host para a sua
            user="root", #Trocar o user para o seu, ou pode deixar o root
            password="123456", #Trocar a senha para a sua
            database="Cozzinhe"
        )
cursor = conexao.cursor()
=======
import mysql.connector
import streamlit as st
conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="Cozzinhe"
        )
cursor = conexao.cursor()
>>>>>>> b2c19ff92db8278fe1315eaafbbe96d5be4f6ba2
