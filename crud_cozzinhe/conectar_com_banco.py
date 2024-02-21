import mysql.connector
import streamlit as st
conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="Cozzinhe"
        )
cursor = conexao.cursor()