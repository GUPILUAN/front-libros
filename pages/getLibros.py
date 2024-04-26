import streamlit as st
import requests as req
import pandas as pd
import os

apiUrl : str | None = os.getenv("API_URL")

if st.button("Menú"):
    st.switch_page("main.py")

apiResponse : req.Response = req.Response()
st.subheader("Libros")
if apiUrl:
    apiResponse  = req.get(f"{apiUrl}/")

libros : list | None = apiResponse.json() if apiResponse.status_code == 200 else None

if libros:
    if len(libros) > 0:
        dataFrameLibros : pd.DataFrame = pd.DataFrame(libros)
        st.dataframe(dataFrameLibros)
    else:
        st.write("No hay libros registrados aun")
        apiResponse.status_code = 404

st.image(f"https://http.cat/{apiResponse.status_code}.jpg", caption= 'Gatito')