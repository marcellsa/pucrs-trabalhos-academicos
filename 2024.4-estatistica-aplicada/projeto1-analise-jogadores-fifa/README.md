# Projeto de Análise dos Jogadores FIFA

Este projeto utiliza dados sobre jogadores de futebol registrados na FIFA para realizar uma análise estatística descritiva com R, visualizando e explorando informações relacionadas às características dos jogadores, como nacionalidade, idade e valor estimado em euros. A análise foi realizada em um Jupyter Notebook com código em R, e este documento fornece uma visão geral do projeto e instruções para sua execução.

## Estrutura do Projeto

```plaintext
.
├── data/
│   ├── Anexo_Projeto_fifa_world_national_teams_versao_oficial_20241virgula.csv  # Dados dos jogadores
├── notebooks/
│   └── analise_jogadores_fifa.ipynb                                            # Notebook principal em R
└── README.md                                                                   # Este arquivo de documentação

## Objetivos do Projeto
- Análise Exploratória: Realizar uma análise descritiva sobre os dados dos jogadores.
- Estatísticas Descritivas: Calcular medidas de posição e variabilidade para variáveis de interesse.
- Visualização de Dados: Utilizar gráficos para identificar padrões e tendências.
- Ajuste de Modelos Probabilísticos: Explorar a possibilidade de ajustar um modelo probabilístico para variáveis contínuas.

## Principais Etapas

1. Configuração Inicial
Para executar o projeto, certifique-se de que as bibliotecas necessárias estão instaladas. O projeto utiliza o R e as seguintes bibliotecas:

install.packages("ggplot2")
install.packages("MASS")
install.packages("scales")

2. Carregamento dos Dados
Os dados estão em formato CSV e contêm informações dos jogadores, como nacionalidade, idade, valor estimado em euros, entre outros. O dicionário de dados fornece uma descrição completa das variáveis e seus tipos.

3. Análise Descritiva
Realizamos uma série de análises descritivas:

- Identificação dos Tipos de Variáveis: foram selecionadas variáveis de cada tipo (nominal, ordinal, discreta e contínua) para a análise.
- Tabelas de Frequência: foi gerado tabelas de frequência para variáveis qualitativas como nationality.
- Medidas de Posição e Variabilidade: for calculado médias, medianas, desvios padrão e outras medidas para variáveis quantitativas.

4. Visualização de Dados
Gráfico de Barras de Nacionalidade

- Foi utilizado um gráfico de barras para visualizar a distribuição dos jogadores por nacionalidade, ordenando as nacionalidades do maior para o menor número de jogadores.

Boxplot do Valor dos Jogadores
- Para examinar a distribuição do valor em euros dos jogadores, foi utilizado um boxplot, removendo valores ausentes.

5. Ajuste de Modelos Probabilísticos
Foi utilizado um histograma da variável age para verificar a adequabilidade de um modelo normal para representar a distribuição da idade dos jogadores. Em seguida, foi ajustado uma curva normal sobre o histograma.

## Resultados Obtidos
- Distribuição de Idades: A análise indica que a idade dos jogadores tem uma distribuição aproximadamente normal.
- Distribuição de Valores: O boxplot dos valores dos jogadores mostra a presença de valores elevados, com alguns outliers que representam jogadores mais valiosos.
- Distribuição por Nacionalidade: Os jogadores são distribuídos de forma desigual entre as nacionalidades, com algumas nações predominando em número.

## Instruções para Execução
1. Clone o Repositório:
  git clone <URL do repositório>

2, Instale as Bibliotecas Necessárias: Execute o código R no notebook para instalar os pacotes.

3. Execute o Notebook: Abra o arquivo analise_jogadores_fifa.ipynb no VS Code e execute célula por célula para reproduzir a análise.

## Conclusões
A análise fornece insights úteis sobre as características dos jogadores de futebol, incluindo distribuições de idade e nacionalidade, além de uma análise do valor estimado dos jogadores. Este projeto pode ser expandido para explorar outras variáveis e aplicar modelos probabilísticos mais complexos.
