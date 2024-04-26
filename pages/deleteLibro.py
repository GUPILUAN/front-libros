import streamlit as st
import requests as req
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menú"):
    st.switch_page("main.py")

st.subheader("Borrar libro")

libroIsbn : str = st.text_input("Ingresa isbn")
verificacion : bool = len(libroIsbn.strip()) > 0 
apiResponse : req.Response = req.Response()

if st.button("Enviar"):
    if verificacion:
        if apiUrl:
            apiResponse = req.delete(f"{apiUrl}/{libroIsbn}")
        if apiResponse.status_code == 200:
            st.write("¡Borrado con éxito!")
    else:
        st.write("Llena todos los campos")
        apiResponse.status_code = 411
    st.image(f"https://http.cat/{apiResponse.status_code}.jpg", caption= 'Gatito')