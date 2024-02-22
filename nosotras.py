import streamlit as st
from PIL import Image

def nosotras():
    st.title("Nuestro equipo")

    col1, col2, col3 = st.beta_columns(3)

 
    col1.write("**Esther García**")
    col1.write("**Linkedin: http://linkedin.com/in/esthergarciagonzalezgg**")
    image1 = Image.open("imagenes/esther.jpeg")
    col1.image(image=image1, width=200)
    st.text("")
    st.text("")


    col2.write("**Beatriz Mimosa**")
    col2.write("**Linkedin: http://linkedin.com/in/beatriz-mimosa**")
    image2 = Image.open("imagenes/bea.jpeg")
    col2.image(image=image2, width=200)
    st.text("")
    st.text("")


    col3.write("**Aida Amoedo**")
    col3.write("**Linkedin: http://linkedin.com/in/aida-amoedo**")
    image3 = Image.open("imagenes/aida.jpeg")
    col3.image(image=image3, width=200)
    st.text("")
    st.text("")

if __name__ == "__main__":
    nosotras()
