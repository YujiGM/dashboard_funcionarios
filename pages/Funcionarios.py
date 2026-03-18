import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.header('Análise dos funcionários!')
st.subheader('Arquivo de estudo sobre os funcionários de uma empresa no Streamlit!')

st.write('Base de dados')
df = pd.read_csv('funcionarios.csv')

#Tratamento de dados

st.write(df.isnull().sum())
df['Salario'] = pd.to_numeric(df['Salario'], errors='coerce')



st.dataframe(df)

dep = df['Departamento'].unique()

col1, col2 = st.columns(2)

with col1:
    dep_op = st.selectbox(
    'Selecione um departamento:',
    dep
)
    df_dep = df[df['Departamento'] == dep_op]
    st.dataframe(df_dep[['Nome','Salario']])
