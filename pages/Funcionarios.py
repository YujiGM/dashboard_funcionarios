import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title('Análise dos :blue[Funcionários!]', width='stretch',text_alignment='center')
st.header('Arquivo de estudo sobre os funcionários de uma empresa no Streamlit!', width='stretch',text_alignment='center')

df = pd.read_csv('funcionarios.csv')

#Tratamento de dados ---------------------------------------------------------

df['Cargo'] = (df['Cargo']
    .str.strip()       
    .str.lower()        
    .str.normalize('NFKD') 
    .str.encode('ascii', errors='ignore')
    .str.decode('utf-8')
)
# ------------------------------------------------------------------------

nome_func = st.text_input('Digite o nome do funcionário')
if nome_func.strip() != "":
        df_func = df[
            df['Nome'].str.lower().str.strip().str.contains(
                nome_func.strip().lower(), na=False
            )
        ]
else:
        df_func = df

st.data_editor(
    df_func,
    column_config={
        'Salario': st.column_config.NumberColumn(
            'Salario (R$)',
            help = 'Salário em Reais.',
            min_value = 0,
            max_value = None,
            step = 1,
            format = "R$ %f",

        )
    },
    hide_index = True,
)

col1, col2 = st.columns(2)

with col1:
        st.metric("Média de idade dos funcionários", df['Idade'].mean(), border = True)
with col2:
        st.metric('Cargo mais comum',df['Cargo'].value_counts().idxmax(), border = True)

col3, col4 = st.columns(2)

with col3:    
    fig = px.pie(
        df,
        names='Senioridade',
        title=f'Distribuição por Senioridade',
        hole=0.3, 
    )

    fig.update_traces(textinfo='percent+label')
    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
with col4:
    df_contrato_salario = df.groupby('Contrato')['Salario'].mean().reset_index()
    df_contrato_salario.columns = ['Departamento', 'Salario Médio']

    st.subheader('Média salarial por contrato')
    st.bar_chart(
        df_contrato_salario,
        x='Departamento',
        y='Salario Médio',
        x_label='Contrato (CLT / PJ / Estágio)',
        y_label='Salário Médio (R$)',
        color='Departamento',
)
