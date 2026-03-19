# 📊 Dashboard de Funcionários

Dashboard interativo desenvolvido com **Streamlit** para análise de dados de funcionários de uma empresa, com visualizações por departamento, salário, sexo e tipo de contrato.

---

## 📁 Estrutura do Projeto

```
dashboard_funcionarios/
├── main.py                  # Página inicial do dashboard
├── funcionarios.csv         # Base de dados dos funcionários
├── requirements.txt         # Dependências do projeto
└── pages/
    ├── funcionarios.py      # Análise geral dos funcionários
    └── Departamentos.py     # Análise por departamento
```

---

## 📄 Páginas

### 🏠 Home (`main.py`)
Página de boas-vindas com navegação para as demais seções e visualização geral da base de dados.

### 💻 Funcionários (`pages/funcionarios.py`)
- Tabela completa dos funcionários com salário formatado em R$
- Filtro por departamento
- Métricas: média salarial e cargo mais comum do setor
- Gráfico de pizza: distribuição por sexo
- Gráfico de barras: salário médio por sexo

### 🏢 Departamentos (`pages/Departamentos.py`)
- Filtro por departamento
- Tabela filtrada com nome, idade, cargo e salário
- Métricas: média salarial e idade média do setor
- Gráfico de barras: salário médio por tipo de contrato
- Gráfico de pizza: distribuição por sexo no departamento selecionado

---

## 🗃️ Base de Dados

O arquivo `funcionarios.csv` contém as seguintes colunas:

| Coluna | Descrição |
|---|---|
| Nome | Nome do funcionário |
| Idade | Idade em anos |
| Salario | Salário em R$ |
| Sexo | M ou F |
| Departamento | Setor da empresa |
| Cargo | Cargo ocupado |
| Senioridade | Nível: Estagiário, Júnior, Pleno, Sênior, Analista, Coordenador, Gerente, Diretoria |
| Contrato | Tipo de contrato: CLT, PJ ou Estágio |

---

## 🚀 Como Executar

**1. Clone o repositório:**
```bash
git clone https://github.com/YujiGM/dashboard_funcionarios.git
cd dashboard_funcionarios
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Execute o Streamlit:**
```bash
streamlit run main.py
```

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

---

## 👤 Autor

**YujiGM** — [github.com/YujiGM](https://github.com/YujiGM)
