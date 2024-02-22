import streamlit as st
from PIL import Image

def nosotras():
    st.title("Nuestro equipo")
    st.write("** Esther García **")
    image = Image.open("imagenes/esther.jpeg")
    resized_image_esther = image.resize((100, 100)) 
    st.image(resized_image_esther, caption="Esther García", use_column_width=True)
    st.text("")


    st.write("**Beatriz Mimosa** ")
    image2 = Image.open("imagenes/bea.jpeg")
    resized_image_bea = image2.resize((100, 100)) 
    st.image(resized_image_bea, caption="Beatriz Mimosa", use_column_width=True)
    st.text("")


    st.write("**Aida Amoedo**")
    image3 = Image.open("imagenes/aida.jpeg")
    resized_image_aida = image3.resize((100, 100)) 
    st.image(resized_image_aida, caption="Aida Amoedo", use_column_width=True)
    st.text("")

if __name__ == "__main__":
    nosotras()
