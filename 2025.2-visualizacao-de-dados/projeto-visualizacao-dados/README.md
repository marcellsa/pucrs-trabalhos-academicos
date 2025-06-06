# 📊 Projeto de Visualização de Dados - Análise de Vendas

Este projeto foi desenvolvido como parte da disciplina de **Visualização de Dados** e tem como objetivo explorar e comunicar insights a partir de dados de transações comerciais.

---

## 📁 Estrutura do Projeto

```
projeto-visualizacao-vendas/
│
├── data/
│ └── SalesDataset.csv # Base de dados original
│
├── notebooks/
│ ├── 1_exploratory_analysis.ipynb # Análise exploratória automatizada
│ └── 2_business_questions.ipynb # Análise visual das questões de negócio
│
└── README.md # Este arquivo

---

## 📌 Objetivos

O objetivo principal deste projeto é utilizar técnicas de visualização de dados para responder a perguntas estratégicas relacionadas a vendas e desempenho de produtos e regiões.

---

## 🔍 Conjunto de Dados

O dataset utilizado (`SalesDataset.csv`) contém transações de vendas incluindo:
- Categorias e subcategorias de produtos
- Valores de vendas (`Amount`) e lucro (`Profit`)
- Informações geográficas (Estado e Cidade)

---

## 🧪 Etapas Realizadas

1. **Análise Exploratória Automatizada**
   - Utilização da biblioteca `ydata_profiling` para avaliação de qualidade dos dados
   - Verificação de dados ausentes, tipos de dados e estatísticas descritivas

2. **Resolução das Questões de Negócio com Visualização**

---

## ❓ Questões de Negócio e Gráficos Utilizados

### 1️⃣ Quais são as 5 subcategorias mais vendidas?
- **Gráfico:** Barras verticais
- **Justificativa:** Os nomes das subcategorias são curtos, o que favorece a visualização vertical. A altura das barras facilita a comparação direta.
- **Insight:** Produtos como *Markers* e *Tables* estão entre os mais vendidos, indicando alta demanda.

---

### 2️⃣ Dentro de cada categoria, quais subcategorias geram mais lucro?
- **Gráfico:** Barras horizontais
- **Justificativa:** Melhor para apresentar nomes de subcategorias e facilitar a leitura de valores de lucro.
- **Insight:** Cada categoria possui uma subcategoria com desempenho financeiro superior, o que pode orientar decisões de foco e promoção.

---

### 3️⃣ Quais cidades apresentam o maior desempenho em vendas e lucro?
- **Gráficos:** Dois gráficos de barras horizontais (um para vendas, outro para lucro)
- **Justificativa:** Cidades têm nomes longos, o que justifica a escolha horizontal para melhor legibilidade.
- **Insight:** Algumas cidades apresentam tanto altos volumes de vendas quanto lucro, sugerindo oportunidades de reforço estratégico nessas regiões.

---

## 📈 Tecnologias Utilizadas

- Python
- Pandas
- Plotly Express
- Jupyter Notebook

---

## 🎯 Conclusão

O projeto possibilitou a prática de técnicas de visualização aplicadas a contextos reais de negócio.  
As representações gráficas ajudaram a comunicar insights valiosos de forma clara e objetiva, apoiando uma tomada de decisão mais eficiente.

---

## 👤 Autor

**Marcel Albuquerque**  
Aluno da disciplina de Visualização de Dados
