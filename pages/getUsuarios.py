import streamlit as st
import requests as req
import pandas as pd

if st.button("Menu"):
    st.switch_page("main.py")

st.subheader("Usuarios")
usuariosResponse : req.Response = req.get("http://3.141.30.188:8000/usuarios/")

usuarios : list | None = usuariosResponse.json()

if usuarios:
    dataFrameUsuarios : pd.DataFrame = pd.DataFrame(usuarios)
    st.dataframe(dataFrameUsuarios)

st.image(f"https://http.cat/{usuariosResponse.status_code}.jpg", caption='Gatito')