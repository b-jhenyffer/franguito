import os
import streamlit as st
from PIL import Image

# Função principal
def app():
    # Título da página
    st.title('Perguntando ao meu xodózão...')

    # Pergunta
    st.write("Aceitas ir pra academia comigo?")

    col1, col2 = st.columns(2) #dividindo a tela em 2 colunas

    # Opções para o usuário
    #resposta = st.radio("Escolha uma opção", ('Logico', 'Não vai dar 111'))

    # Caminhos absolutos para as imagens
    bora_path = 'data/bora.jpg'
    mise_path = 'data/mise.png'

    with col1:
        if st.button('Má, LÓGICO'):
            st.write("Então bora? Agora?")
            img = Image.open(bora_path)
            st.image(img, caption=' ', use_container_width=bool)

    
    with col2:
        if st.button('Não'):
            st.write("Misericuerdia, estoy mirando un franguito")
            img = Image.open(mise_path)
            st.image(img, caption=' ', use_container_width=bool)

# Rodar a aplicação
if __name__ == '__main__':
    app()
