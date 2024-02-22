import streamlit as st
from PIL import Image

def nosotras():
    st.title("Nuestro equipo")

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.write("**Esther García**")
        st.write("**Linkedin: http://linkedin.com/in/esthergarciagonzalezgg**")
        image = Image.open("imagenes/esther.jpeg")
        st.image(image=image, width=200)
        st.text("")
        st.text("")

    with col2:
        st.write("**Beatriz Mimosa**")
        st.write("**Linkedin: http://linkedin.com/in/beatriz-mimosa**")
        image2 = Image.open("imagenes/bea.jpeg")
        st.image(image=image2, width=200)
        st.text("")
        st.text("")

    with col3:
        st.write("**Aida Amoedo**")
        st.write("**Linkedin: http://linkedin.com/in/aida-amoedo**")
        image3 = Image.open("imagenes/aida.jpeg")
        st.image(image=image3, width=200)
        st.text("")
        st.text("")

if __name__ == "__main__":
    nosotras()
