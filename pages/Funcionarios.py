import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Análise dos :blue[Funcionários!]', width='stretch',text_alignment='center')
st.header('Arquivo de estudo sobre os funcionários de uma empresa no Streamlit!', width='stretch',text_alignment='center')

df = pd.read_csv('funcionarios.csv')

#Tratamento de dados ---------------------------------------------------------
df_dep_salarioM = 0
maior_sal =0
maior_sal_cargo = ""

st.write('Funcionários')
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


#Tratamento de dados ---------------------------------------------------------

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

with col2:
    idx_maior = df_dep['Salario'].idxmax()
    maior_sal = df_dep.loc[idx_maior, 'Salario']
    maior_sal_cargo = df_dep.loc[idx_maior, 'Cargo'] 

    col2.metric('Média salarial do setor', f"R$ {df_dep_salarioM:.2f}", border = True)
    
df_sexo_salario = df.groupby('Sexo')['Salario'].mean().reset_index()
df_sexo_salario.columns = ['Sexo', 'Salario Médio']

st.header('Média Salarial por Sexo', width='stretch',text_alignment='center')

st.bar_chart(
    df_sexo_salario,
    x='Sexo',
    y='Salario Médio',
    x_label='Sexo',
    y_label='Salário Médio (R$)',
    color='Sexo',
)