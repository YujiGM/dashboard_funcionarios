import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Olá, Bem Vindo a :green[Dashboard Funcionários!]', width='stretch', text_alignment='center')
st.header('Esta é a pagina inicial do meu dashboard no Streamlit.', width='stretch', text_alignment='center')
st.subheader('Você pode tanto checar a base de dados quanto olhar a análise realizada.', width='stretch', text_alignment='center')
st.subheader('Este relatório apresenta uma análise completa dos funcionários da empresa, incluindo métricas salariais, distribuição por sexo, senioridade e tipo de contrato — organizados por departamento.', width='stretch', text_alignment='center')

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/Funcionarios.py", label="Funcionários", icon='🚹',width='stretch')
with col2:
    st.page_link("pages/Departamentos.py", label="Departamentos", icon='🏢',width='stretch')
    