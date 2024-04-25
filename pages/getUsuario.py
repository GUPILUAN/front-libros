import streamlit as st
import requests as req
from models.usuario import Usuario
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menu"):
    st.switch_page("main.py")

st.subheader("Buscar usuario")


email : str = st.text_input('Escribe el email')
usuariosResponse : req.Response = req.Response()
presionado : bool = False

if st.button('Buscar'):
    if apiUrl:
        usuariosResponse = req.get(f"{apiUrl}/{email if len(email.strip()) > 0 else ' '}")
    presionado = True

if presionado:
    st.subheader("Usuario:")
    usuarioEncontrado : dict| None = usuariosResponse.json() if usuariosResponse.status_code == 200 else None
    if usuarioEncontrado:
        usuario : Usuario = Usuario()
        usuario.nombre = usuarioEncontrado["nombre"]
        usuario.email = usuarioEncontrado["email"]
        usuario.password = usuarioEncontrado["password"]
        st.write(str(usuario))
        usuariosResponse.status_code = 302
    else:
        st.write("No existe")

    st.image(f"https://http.cat/{usuariosResponse.status_code}.jpg", caption='Gatito')