import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.title("Frontend libros")
st.header("---CALLING REST API---")

if st.button("Todos los libros"):
    st.switch_page("pages/getLibros.py")

if st.button("Encontrar un libro"):
    st.switch_page("pages/getLibro.py")

if st.button("Crear un libro"):
    st.switch_page("pages/createLibro.py")

if st.button("Actualizar un libro"):
    st.switch_page("pages/updateLibro.py")

if st.button("Borrar un libro"):
    st.switch_page("pages/deleteLibro.py")
