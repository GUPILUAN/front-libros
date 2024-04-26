import streamlit as st
import requests as req
from models.libroModel import Libro
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menu"):
    st.switch_page("main.py")
    
st.subheader("Actualizar libro")

isbnBuscado : str = st.text_input("Ingresa isbn a buscar")
verificacion1 : bool = len(isbnBuscado.strip()) > 0 
libro : Libro = Libro()
libroTitulo : str = st.text_input("Ingresa nombre")
libroAutor : str = st.text_input("Ingresa autor")
libroIsbn : str = st.text_input("Ingresa isbn")
verificacion2 : bool = len(libroTitulo.strip()) > 0 and len(libroAutor.strip()) > 0 and len(libroIsbn.strip()) > 0
apiResponse : req.Response = req.Response()
if st.button("Enviar"):
    if(verificacion1 and verificacion2):
        libro.titulo = libroTitulo
        libro.autor = libroAutor
        libro.isbn = libroIsbn
        if apiUrl:
            apiResponse = req.put(f"{apiUrl}/{isbnBuscado}", json= libro.convertirToDict())
        if apiResponse.status_code == 200:
            st.write("¡Actualizado con éxito!")
    else:
        st.write("Llena todos los campos")
        apiResponse.status_code = 411
    st.image(f"https://http.cat/{apiResponse.status_code}.jpg", caption='Gatito')