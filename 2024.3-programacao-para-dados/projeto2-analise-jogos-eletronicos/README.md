# Análise de Jogos da Steam

Este projeto foi desenvolvido como parte de uma disciplina da faculdade, focando na análise de dados de jogos publicados na plataforma Steam. O objetivo principal é explorar diferentes aspectos relacionados aos jogos, como suporte a sistemas operacionais, tendências de lançamento por gênero, e a relação entre preço e popularidade, utilizando técnicas de análise de dados e visualização.

## Objetivos do Projeto

O objetivo deste projeto é extrair insights significativos sobre o mercado de jogos da Steam. A análise busca responder perguntas como:

- Qual o percentual de jogos que possuem suporte para cada sistema operacional?
- Como tem sido a tendência de lançamentos de jogos single-player dos gêneros Indie e Estratégia ao longo dos anos?
- Existe alguma relação entre o preço dos jogos e o número de avaliações positivas recebidas?

## Perguntas de Negócio

1. **Percentual de jogos que possuem suporte para cada sistema operacional:**  
   Qual a distribuição percentual de jogos que suportam Windows, Mac e Linux?

2. **Tendência de lançamentos de jogos Indie e Estratégia single-player entre 2010 e 2020:**  
   Como evoluiu o número de jogos lançados nos gêneros Indie e Estratégia ao longo dos anos?

3. **Relação entre o preço dos jogos e o número de avaliações positivas recebidas:**  
   Existe uma correlação significativa entre o preço do jogo e o número de avaliações positivas?

4. **Média de preços dos jogos por faixa etária mínima recomendada:**  
   Qual é a média de preços dos jogos agrupados por faixa etária mínima recomendada?

## Conjunto de Dados

O conjunto de dados utilizado para este projeto contém informações detalhadas sobre mais de 70.000 jogos disponíveis na plataforma Steam, coletadas em maio de 2023. Algumas das colunas incluídas são:

- **AppID**: Identificador único do jogo.
- **Name**: Nome do jogo.
- **Release date**: Data de lançamento.
- **Price**: Preço do jogo em USD.
- **Genres**: Gênero(s) do jogo.
- **Platforms**: Plataformas suportadas (Windows, Mac, Linux).
- **Positive**: Número de avaliações positivas.
- **Negative**: Número de avaliações negativas.
- **... e outros atributos.**

## Ferramentas e Bibliotecas Utilizadas

- **Linguagem**: Python 3
- **Bibliotecas**: 
  - `pandas` para manipulação e análise de dados
  - `matplotlib` e `seaborn` para visualização de dados

## Estrutura do Projeto

A estrutura de diretórios do projeto é a seguinte:

projeto2-analise-jogos-eletronicis/ │ ├── data/ │ └── steam_games.csv # Arquivo de dados original │ │ ├── notebooks/ │ └── steam_analysis.ipynb # Jupyter Notebook para exploração e execução do código │ └── README.md # Documentação do projeto

## Instruções para Execução

1. **Clonando o Repositório**

   Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/projeto2-analise-jogos-eletronicos.git
   cd projeto2-analise-jogos-eletronis

## Instalando Dependências


   ```bash
   pip install -r requirements.txt

## Créditos

Este projeto faz parte de uma disciplina de Programação para Dados e foi desenvolvido para fins acadêmicos.