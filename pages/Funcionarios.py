import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Análise dos funcionários!')
st.header('Arquivo de estudo sobre os funcionários de uma empresa no Streamlit!')

df = pd.read_csv('funcionarios.csv')

#Tratamento de dados
df_dep_salarioM = 0

st.write('Base de Dados')
st.data_editor(
    df,
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

dep = df['Departamento'].unique()

col1, col2 = st.columns(2)

with col1:
    dep_op = st.selectbox(
        'Selecione um departamento:',
        dep
    )
    df_dep = df[df['Departamento'] == dep_op]

    st.data_editor(     
        df_dep[['Nome', 'Cargo', 'Salario']],
        column_config={
            'Salario': st.column_config.NumberColumn(
                'Salario (R$)',
                help='Salário em Reais.',
                min_value=0,
                max_value=None,
                step=1,
                format="R$ %f",
            )
        },
        hide_index=True,
        disabled=True, 
    )

    df_dep_salarioM = df_dep['Salario'].mean()
    st.write(f'Média Salarial do Setor: R$ {df_dep_salarioM:.2f}')