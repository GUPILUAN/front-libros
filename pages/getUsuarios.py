import streamlit as st
import requests as req
import pandas as pd
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menu"):
    st.switch_page("main.py")

usuariosResponse : req.Response = req.Response()
st.subheader("Usuarios")
if apiUrl:
    usuariosResponse  = req.get(apiUrl)

usuarios : list | None = usuariosResponse.json() if usuariosResponse.status_code == 200 else None

if usuarios:
    dataFrameUsuarios : pd.DataFrame = pd.DataFrame(usuarios)
    st.dataframe(dataFrameUsuarios)

st.image(f"https://http.cat/{usuariosResponse.status_code}.jpg", caption='Gatito')