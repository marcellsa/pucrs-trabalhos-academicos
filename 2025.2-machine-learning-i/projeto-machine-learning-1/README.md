# Projeto de Machine Learning I – Fase 1

**Disciplina:** Machine Learning I  
**Dataset:** ATLANTIC FLOWER-INVERTEBRATE INTERACTIONS

---

## 📌 Objetivo

Este projeto tem como objetivo aplicar os conceitos de Análise Exploratória de Dados (EDA) e Preparação de Dados para o desenvolvimento de um modelo de classificação na Fase 2. O foco da Fase 1 é garantir que os dados estejam prontos para modelagem.

---

## 🧪 Etapas realizadas na Fase 1

1. **Análise Exploratória (EDA)**
   - Visualização de dados (boxplots, histogramas, gráficos de contagem)
   - Correlação entre variáveis

2. **Formatação dos atributos**
   - Unificação de formatos e padronização de representações

3. **Transformação dos dados**
   - Conversão de atributos categóricos para o formato numérico

4. **Tratamento de dados faltantes**
   - Preenchimento com K-means e, quando necessário, mediana global
   - Exclusão de colunas com baixa relevância e alta ausência de dados

5. **Tratamento de outliers**
   - Identificação via boxplots
   - Tratamento de atributos críticos

6. **Reescalonamento dos dados**
   - Padronização com `StandardScaler` 

---

## 📁 Conteúdo da pasta

```text
projeto-machine-learning-1/
│
├── data/
│   ├── raw/                         # Dataset original (não modificado)
│   └── processed/
│       └── dataset_fase1_tratado.csv   # Dataset limpo e preparado
│
├── notebooks/
│   └── ML_Fase1.ipynb              # Notebook com todas as análises e etapas
│
└── README.md                       # Documento atual com descrição do projeto

---

## ✅ Pronto para a Fase 2

O dataset final (`dataset_fase1_tratado.csv`) está pronto para ser utilizado em algoritmos de classificação binária com foco na variável `invertebrate_origins`.

---