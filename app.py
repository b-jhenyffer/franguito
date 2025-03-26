import os
import streamlit as st
from PIL import Image

# Função principal
def app():
    # Título da página
    st.title('Sim ou Não?')

    # Pergunta
    st.write("Você vai pra academia comigo?")

    col1, col2 = st.columns(2) #dividindo a tela em 2 colunas

    # Opções para o usuário
    #resposta = st.radio("Escolha uma opção", ('Logico', 'Não vai dar 111'))

    # Caminhos absolutos para as imagens
    dog_image_path = '/Users/jhenyfferborges/Documents/Projects/frango2/franguito/data/bora.jpg'
    frango_image_path = '/Users/jhenyfferborges/Documents/Projects/frango2/franguito/data/mise.jpg'

    with col1:
        if st.button('Má, LÓGICO'):
            st.write("Então bora? Agora?")
            img = Image.open('/Users/jhenyfferborges/Documents/Projects/popopo/frangudo/data/bora.jpg')
            st.image(img, caption=' ', use_container_width=bool)

    
    with col2:
        if st.button('Não'):
            st.write("Misericuerdia, estoy mirando um franguito")
            img = Image.open('/Users/jhenyfferborges/Documents/Projects/popopo/frangudo/data/mise.jpg')
            st.image(img, caption=' ', use_container_width=bool)

# Rodar a aplicação
if __name__ == '__main__':
    app()
