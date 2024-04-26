import streamlit as st
import requests as req
from models.libroModel import Libro
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menú"):
    st.switch_page("main.py")
    
st.subheader("Crear libro")

libro : Libro = Libro()
libroTitulo : str = st.text_input("Ingresa titulo")
libroAutor : str = st.text_input("Ingresa autor")
libroIsbn : str = st.text_input("Ingresa isbn")
verificacion : bool = len(libroTitulo.strip()) > 0 and len(libroAutor.strip()) > 0 and len(libroIsbn.strip()) > 0
apiResponse : req.Response = req.Response()

if st.button("Enviar"):
    if verificacion:
        libro.titulo = libroTitulo
        libro.autor = libroAutor
        libro.isbn = libroIsbn
        if apiUrl:
            apiResponse = req.post(apiUrl, json= libro.convertirToDict())
        if apiResponse.status_code == 200:
            apiResponse.status_code = 201
            st.write("¡Libro creado con éxito!")
        else:
            st.write("Error al enviar los datos :(")
    else:
        st.write("Llena todos los campos")
        apiResponse.status_code = 411
    st.image(f"https://http.cat/{apiResponse.status_code}.jpg", caption= 'Gatito')