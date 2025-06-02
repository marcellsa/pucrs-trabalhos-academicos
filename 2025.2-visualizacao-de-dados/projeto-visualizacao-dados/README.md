# 📊 Análise de Dados de Vendas

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-brightgreen)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-orange)

## 📂 Estrutura do Projeto
meu_projeto/
├── data/
│ └── raw/ # Dados brutos em CSV
│ └── SalesDataset.csv # Dataset principal
├── notebooks/
│ ├── 1_exploratory_analysis.ipynb # Análise exploratória
│ └── 2_business_questions.ipynb # Análise de negócios
├── reports/
│ └── exploratory_report.html # Relatório automático
├── .gitignore
├── requirements.txt
└── README.md


## 🎯 Objetivos

1. Identificar padrões de vendas por categoria e região
2. Analisar a relação entre volume de vendas e lucratividade
3. Gerar insights acionáveis para decisões comerciais

## 🔧 Pré-requisitos

- Python 3.12+
- Jupyter Notebook
- Bibliotecas listadas em `requirements.txt`

## 🚀 Como Usar

```bash
# 1. Clonar repositório
git clone [URL_DO_REPOSITORIO]

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Executar notebooks
jupyter notebook

📈 Análises Realizadas
Notebook 1: Análise Exploratória
Qualidade dos dados

Estatísticas descritivas

Identificação de outliers

Notebook 2: Questões de Negócio
Top 5 categorias/subcategorias por volume de vendas

Subcategorias mais lucrativas em cada categoria

Desempenho por estado/cidade (vendas e lucro)

📌 Exemplo de Visualização
import plotly.express as px
fig = px.bar(top_products, x='Sub-Category', y='Amount')
fig.show()

📝 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.