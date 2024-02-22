import streamlit as st
from PIL import Image

def nosotras():
    st.title("Nuestro equipo")
    st.write("** Esther García **")
    image = Image.open("/home/hacker/PycharmProjects/proy3/imagenes/esther.jpeg")
    st.image(image, caption="Esther García", use_column_width=True)
    st.text("")


    st.write("**Beatriz Mimosa** ")
    image2 = Image.open("/home/hacker/PycharmProjects/proy3/imagenes/bea.jpeg")
    st.image(image2, caption="Beatriz Mimosa", use_column_width=True)
    st.text("")


    st.write("**Aida Amoedo**")
    image3 = Image.open("/home/hacker/PycharmProjects/proy3/imagenes/aida.jpeg")
    st.image(image3, caption="Aida Amoedo", use_column_width=True)
    st.text("")

if __name__ == "__main__":
    nosotras()
