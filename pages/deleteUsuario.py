import streamlit as st
import requests as req

if st.button("Menu"):
    st.switch_page("main.py")

st.subheader("Borrar Usuario")

userEmail : str = st.text_input("Ingresa email")
verificacion : bool = len(userEmail.strip()) > 0 
usuariosResponse : req.Response = req.Response()
if st.button("Enviar"):
    if(verificacion):
        usuariosResponse = req.delete(f"http://3.141.30.188:8000/usuarios/{userEmail}")
        if usuariosResponse.status_code == 200:
            st.write("¡Borrado con éxito!")
    else:
        st.write("Llena todos los campos")
        usuariosResponse.status_code = 411
    st.image(f"https://http.cat/{usuariosResponse.status_code}.jpg", caption='Gatito')