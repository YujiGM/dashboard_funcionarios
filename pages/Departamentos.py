import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title('Análise dos :red[Departamentos!]', width='stretch',text_alignment='center')
st.header('Arquivo de estudo sobre os departamentos de uma empresa no Streamlit!', width='stretch',text_alignment='center')

df = pd.read_csv('funcionarios.csv')

#Tratamento de dados ---------------------------------------------------------
df_dep_salarioM = 0
maior_sal =0
maior_sal_cargo = ""
df_dep_idadeM = 0
dep = df['Departamento'].unique()

df['Cargo'] = (df['Cargo']
    .str.strip()       
    .str.lower()        
    .str.normalize('NFKD') 
    .str.encode('ascii', errors='ignore')
    .str.decode('utf-8')
)
# ---------------------------------------------------------

dep_op = st.selectbox(
        'Selecione um departamento:',
        dep
    )
df_dep = df[df['Departamento'] == dep_op]

st.data_editor(     
    df_dep[['Nome', 'Idade','Cargo', 'Salario']],
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
df_dep_idadeM = df_dep['Idade'].mean()

cargo_mais_comum = df_dep['Senioridade'].value_counts().idxmax()
quantidade = df_dep['Senioridade'].value_counts().max()


idx_maior = df_dep['Salario'].idxmax()
maior_sal = df_dep.loc[idx_maior, 'Salario']
maior_sal_cargo = df_dep.loc[idx_maior, 'Cargo'] 

col1, col2 = st.columns(2)

with col1:
    col1.metric('Média salarial do setor', f"R$ {df_dep_salarioM:.2f}", border = True, format = 'localized')
with col2:
    col2.metric('Idade média do setor',f'{df_dep_idadeM:.2f}', border = True, delta_arrow = 'off')

df_contrato_salario = df_dep.groupby('Contrato')['Salario'].mean().reset_index()
df_contrato_salario.columns = ['Departamento', 'Salario Médio']

st.header('Média Salarial por tipo de contrato', width='stretch',text_alignment='center')

st.bar_chart(
    df_contrato_salario,
    x='Departamento',
    y='Salario Médio',
    x_label='Contrato (CLT / PJ / Estágio)',
    y_label='Salário Médio (R$)',
    color='Departamento',
)

fig = px.pie(
    df_dep,
    names='Sexo',
    title=f'Distribuição por Sexo — {dep_op}',
    hole=0.3, 
)

fig.update_traces(textinfo='percent+label')
fig.update_layout(showlegend=False)

st.plotly_chart(fig, use_container_width=True)