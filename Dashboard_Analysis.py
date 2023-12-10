import pandas as pd
import streamlit as st

st.set_page_config(
        layout="wide",
        page_title="Airbnb NYC"
)


df = pd.read_csv("C:/Users/reneb/OneDrive/Área de Trabalho/Airbnb/archive (4)/train.csv")
Cidade = st.sidebar.selectbox("Cidades",df["neighbourhood_group"].value_counts().index)
df_Cidade = df[df["neighbourhood_group"] == Cidade]
Bairro = st.sidebar.selectbox("Bairros",df_Cidade["neighbourhood"].value_counts().index)
df_Bairro = df_Cidade[df_Cidade["neighbourhood"] == Bairro]
zoom = st.sidebar.slider(label= "Zoom do Mapa",
                  min_value=1,
                  max_value=20, 
                  value=13)
df_Quarto = df_Bairro.groupby(["room_type"])["price"].mean().to_frame().reset_index()
df_Quarto.columns = ["Tipo de Imóvel", "Preço Médio USD ($)"]

df_AnaliseBairro = df_Cidade.groupby(['neighbourhood'])['price'].mean().to_frame().reset_index().sort_values('price', ascending = False)
df_AnaliseBairro.columns = ["Bairro", "Preço Médio USD ($)"]

col1, col2 = st.columns(2)
col1.bar_chart(df_Quarto, x = "Tipo de Imóvel", y = "Preço Médio USD ($)")
col2.bar_chart(df_AnaliseBairro, x = "Bairro", y = "Preço Médio USD ($)")


st.map(df_Bairro,
    latitude='latitude',
    longitude='longitude',
    size = 0.2,
    zoom = zoom)