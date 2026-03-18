import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Olá, Bem Vindo ao Home!')
st.header('Esta é a pagina inicial do meu dashboard no Streamlit.')
st.write('Você pode tanto checar a base de dados quanto olhar a análise realizada.')
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/funcionarios.py", label= "Análise - Funcionários", icon="💻")

st.header('Header')
st.subheader('Este é um subheader')
st.text('texto simples')
st.markdown('Este texto é em **negrito**')

data = {
    'Nome':['Ana','Bruno','Caio'],
    'Idade':[32,21,55],
    'Salario':[2500,3000,1500]

}

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salario'])
st.pyplot(fig)

if st.button('Clique Aqui!'):
    st.write('Botão clicado vez!')

idade = st.slider('Selecione sua idade', 0, 100, 25)
st.write(f'Idade Selecionada: {idade}')

opcao = st.selectbox(
    'Escolha um departamento: ',
    ['RH', 'TI', 'Vendas']
)
st.write(f'Departamento escolhido: {opcao}')

df_func = pd.read_csv('funcionarios.csv')
df_func.columns = df_func.columns.str.strip()

st.dataframe(df_func)
idade_min = st.slider('Idade mínima',0, 100, 30)

df_filtrado = df_func[df_func['Idade'] > idade_min]
st.dataframe(df_filtrado)

col1, col2 = st.columns(2)

with col1:
    st.header('Coluna 1')
    st.write('Conteúdo da coluna 1.')

with col2:
    st.header('Coluna 2')
    st.write('Conteúdo da coluna 2.')

st.page_link("pages/funcionarios.py", label="Home", icon="🏠")

st.sidebar.header('Filtros.')
idade_min = st.sidebar.slider('Idade Mínima',0,100,30)
