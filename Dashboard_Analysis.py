import pandas as pd
import streamlit as st


df = pd.read_csv("C:/Users/reneb/OneDrive/Área de Trabalho/Airbnb/archive (4)/train.csv")
Cidade = st.sidebar.selectbox("Cidades",df["neighbourhood_group"].value_counts().index)
df_Cidade = df[df["neighbourhood_group"] == Cidade]
Bairro = st.sidebar.selectbox("Bairros",df_Cidade["neighbourhood"].value_counts().index)
df_Bairro = df_Cidade[df_Cidade["neighbourhood"] == Bairro]
zoom = st.sidebar.slider(label= "Zoom do Mapa",
                  min_value=1,
                  max_value=20)
st.map(df_Bairro,
    latitude='latitude',
    longitude='longitude',
    size = 0.2,
    zoom = zoom
)