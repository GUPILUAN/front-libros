import streamlit as st
import requests as req
from models.usuario import Usuario
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menu"):
    st.switch_page("main.py")
    
st.subheader("Actualizar Usuario")

userEmailBuscado : str = st.text_input("Ingresa email a buscar")
verificacion1 : bool = len(userEmailBuscado.strip()) > 0 
usuario : Usuario = Usuario()
userNombre : str = st.text_input("Ingresa nombre")
userEmail : str = st.text_input("Ingresa email")
userPass : str = st.text_input("Ingresa password")
verificacion2 : bool = len(userNombre.strip()) > 0 and len(userEmail.strip()) > 0 and len(userPass.strip()) > 0
usuariosResponse : req.Response = req.Response()
if st.button("Enviar"):
    if(verificacion1 and verificacion2):
        usuario.nombre = userNombre
        usuario.email = userEmail
        usuario.password = userPass
        if apiUrl:
            usuariosResponse = req.put(f"{apiUrl}/{userEmailBuscado}", json=usuario.convertirToDict())
        if usuariosResponse.status_code == 200:
            st.write("¡Actualizado con éxito!")
    else:
        st.write("Llena todos los campos")
        usuariosResponse.status_code = 411
    st.image(f"https://http.cat/{usuariosResponse.status_code}.jpg", caption='Gatito')