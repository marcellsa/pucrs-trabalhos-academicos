
# Projeto de Machine Learning I – Fases 1 e 2

**Disciplina:** Machine Learning I  
**Dataset:** ATLANTIC FLOWER-INVERTEBRATE INTERACTIONS  

---

## Objetivo

Desenvolver uma solução de classificação binária para prever a origem dos invertebrados (native ou non-native), aplicando as etapas de análise exploratória, preparação dos dados e criação de modelos de Machine Learning.

---

## Etapas realizadas na Fase 1

1. **Análise Exploratória (EDA)**
   - Visualização com histogramas, boxplots, heatmap de correlação e gráficos de contagem.
   - Identificação de dados faltantes e outliers.

2. **Preparação e transformação dos dados**
   - Unificação de representações e formatos.
   - Conversão de atributos categóricos em numéricos.
   - Padronização de atributos numéricos com `StandardScaler`.
   - Tratamento de dados faltantes com K-means + mediana.
   - Exclusão de colunas irrelevantes.

---

## Etapas realizadas na Fase 2

1. **Balanceamento da variável alvo**
   - Aplicação de oversampling da classe minoritária com `resample`.

2. **Treinamento dos modelos**
   - Teste de quatro algoritmos: Decision Tree, MLP, Random Forest e Regressão Logística.
   - Ajuste de hiperparâmetros via `GridSearchCV` com validação cruzada (cv=5).

3. **Avaliação**
   - Métricas coletadas: Acurácia, Precisão, Recall, F1-score.
   - Análise da matriz de confusão.
   - Comparação gráfica dos modelos.

4. **Conclusão**
   - O Random Forest foi o modelo com melhor desempenho (acima de 99% em todas as métricas).
   - A Decision Tree também teve ótimo resultado, mas com maior risco de overfitting.
   - MLP e Regressão Logística tiveram desempenho inferior.
   - Apesar do alto desempenho dos modelos, destacamos a necessidade de investigar possíveis sinais de overfitting ou viés nos dados.

---

## Estrutura do projeto

```text
projeto-machine-learning-1/
│
├── data/
│   ├── raw/                         
│   └── processed/
│       ├── dataset_fase1_tratado.csv    
│       └── dataset_fase2_balanceado.csv 
│
├── notebooks/
│   ├── ML_Fase1.ipynb              
│   └── ML_Fase2.ipynb              
│
└── README.md                       
```

---

## Status

O projeto foi concluído com sucesso, entregando um classificador binário robusto e validado.
