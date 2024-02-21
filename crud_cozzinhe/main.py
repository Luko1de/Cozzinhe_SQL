import streamlit as st

# informe a senha do seu mysql
senha = "123"
# Configurações
st.set_page_config(page_title='CoZZinhe', page_icon=':fork_and_knife:', layout='wide')

# Estilo CSS para personalização
st.markdown(
    """
    <style>
    .title {
        font-family: 'Arial Black', sans-serif;
        font-size: 48px;
        text-align: center;
        color: #FF5733;
        display: flex;
        align-items: center;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    .logo {
        max-width: 60%;
    }
    .description {
        font-size: 24px;
        text-align: center;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título e descrição do projeto
st.title(':fork_and_knife: CoZZinhe')

st.write("""
O CoZZinhe é um projeto desenvolvido para gerenciar receitas e ingredientes de forma fácil e organizada.
Você pode adicionar, editar, excluir e visualizar receitas, bem como gerenciar ingredientes usados nessas receitas.
Aproveite para explorar as funcionalidades disponíveis!
""")

# Logo

