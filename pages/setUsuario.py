import streamlit as st
import requests as req
from models.usuario import Usuario

if st.button("Menu"):
    st.switch_page("main.py")
    
st.subheader("Crear Usuario")

usuario : Usuario = Usuario()
userNombre : str = st.text_input("Ingresa nombre")
userEmail : str = st.text_input("Ingresa email")
userPass : str = st.text_input("Ingresa password")
verificacion : bool = len(userNombre.strip()) > 0 and len(userEmail.strip()) > 0 and len(userPass.strip()) > 0
usuariosResponse : req.Response = req.Response()
if st.button("Enviar"):
    if(verificacion):
        usuario.nombre = userNombre
        usuario.email = userEmail
        usuario.password = userPass
        usuariosResponse = req.post('http://3.141.30.188:8000/usuarios/', json=usuario.convertirToDict())
        if usuariosResponse.status_code == 200:
            usuariosResponse.status_code = 201
            st.write("¡Usuario creado con éxito!")
        else:
            st.write("Error al enviar datos")
    else:
        st.write("Llena todos los campos")
        usuariosResponse.status_code = 411
    st.image(f"https://http.cat/{usuariosResponse.status_code}.jpg", caption='Gatito')