import streamlit as st
from PIL import Image

def nosotras():
    st.title("Nuestro equipo")
    st.write("**Esther García**")
    image = Image.open("imagenes/esther.jpeg")
    st.image(image=image, width=200)
    st.text("")
    st.text("")


    st.write("**Beatriz Mimosa** ")
    image2 = Image.open("imagenes/bea.jpeg")
    st.image(image=image2, width=200)
    st.text("")
    st.text("")


    st.write("**Aida Amoedo**")
    st.write("**Linkedin: http://linkedin.com/in/aida-amoedo**")
    image3 = Image.open("imagenes/aida.jpeg")
    st.image(image=image3, width=200)
    st.text("")
    st.text("")

if __name__ == "__main__":
    nosotras()
