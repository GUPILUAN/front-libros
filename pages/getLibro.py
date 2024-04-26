import streamlit as st
import requests as req
from models.libroModel import Libro
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menú"):
    st.switch_page("main.py")

st.subheader("Buscar libro")

isbn : str = st.text_input('Escribe el isbn')
apiResponse : req.Response = req.Response()
presionado : bool = False

if st.button('Buscar'):
    if apiUrl:
        apiResponse = req.get(f"{apiUrl}/{isbn if len(isbn.strip()) > 0 else ' '}")
    presionado = True

if presionado:
    st.subheader("Libro:")
    libroEncontrado : dict| None = apiResponse.json() if apiResponse.status_code == 200 else None
    if libroEncontrado:
        libro : Libro = Libro()
        libro.titulo = libroEncontrado["titulo"]
        libro.autor = libroEncontrado["autor"]
        libro.isbn = libroEncontrado["isbn"]
        st.write(str(libro))
        apiResponse.status_code = 302
    else:
        st.write("No existe")

    st.image(f"https://http.cat/{apiResponse.status_code}.jpg", caption= 'Gatito')