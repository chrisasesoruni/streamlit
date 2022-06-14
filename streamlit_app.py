# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import pip
pip.main(["install", "openpyxl"])

df_bonilla = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Bonilla.xlsx', header= 0) 
df_miraflores= pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Ov.Miraflores.xlsx', header= 0) 
# df = pd.read_excel(...)  # will work for Excel files

st.title("Tabla Bonilla")  # add a title
st.write(df_bonilla[:,6,14].hist())  # visualize my dataframe in the Streamlit app
st.title("Tabla Miraflores")  # add a title
st.write(df_miraflores)  # visualize my dataframe in the Streamlit app
