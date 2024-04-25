import streamlit as st

st.title("Frontend usuarios")
st.header("---CALLING REST API---")

if st.button("Todos los usuarios"):
    st.switch_page("pages/getUsuarios.py")

if st.button("Encontrar un usuario"):
    st.switch_page("pages/getUsuario.py")

if st.button("Crear un usuario"):
    st.switch_page("pages/setUsuario.py")

if st.button("Actualizar un usuario"):
    st.switch_page("pages/updateUsuario.py")

if st.button("Borrar un usuario"):
    st.switch_page("pages/deleteUsuario.py")
