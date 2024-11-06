# Análise Populacional e Econômica Global

Este projeto faz parte da disciplina de **Coleta e Preparação de Dados** da **PUCRS** e tem como objetivo consolidar dados populacionais e econômicos de diversos países, integrando informações de uma API de dados geográficos e um arquivo CSV com dados históricos de PIB. O resultado final é um arquivo CSV contendo uma linha para cada país, com as seguintes colunas:

- `codigo`: Código do país
- `nome`: Nome do país
- `populacao`: População atual
- `capital`: Capital do país
- `area`: Área do país
- `continente`: Continente ao qual o país pertence
- `PIB`: Colunas com o PIB do país para cada ano de 1960 até 2021

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

projeto/ ├── environment/ │ └── requirements.txt # Arquivo com dependências do projeto ├── src/ │ ├── 1_coleta_e_consolidacao_dados.ipynb # Notebook do projeto │ └── ... # Outros módulos de apoio, se necessário ├── data/ │ ├── country.json # Dados brutos coletados da API │ ├── gdp_data.csv # Dados de PIB (fonte CSV) │ └── ... # Outros arquivos de dados, se necessário ├── outputs/ │ └── dados_paises_pibs_consolidado.csv # Arquivo CSV final consolidado └── README.md # Documentação do projeto


## Configuração do Ambiente

### Pré-requisitos

- Python 3.7 ou superior
- `pip` para gerenciar pacotes Python

### Instalação das Dependências

1. Clone este repositório:

   ```bash
   git clone <URL_do_repositório>
   cd projeto

2. Instale as dependências listadas no requirements.txt:

   ```bash
   git clone <URL_do_repositório>
   cd projeto

## Fontes de Dados

API de Informações Geográficas: Utilizamos uma API para obter dados como nome do país, população, capital, área e continente. Esses dados são armazenados no arquivo api_data.json.

Dados de PIB (CSV): Um arquivo CSV contendo dados históricos do PIB dos países, com uma coluna para cada ano de 1960 a 2021. Esse arquivo é chamado gdp_data.csv.

## Funcionamento do Projeto

### Passo a Passo do Projeto

1. Coleta de Dados:

No arquivo 1_coleta_e_consolidacao_dados.ipynb é realizado uma requisição à API e salvo os dados relevantes em um arquivo JSON (ex: api_data.json).
O CSV de PIB (gdp_data.csv) é carregado no projeto a partir da pasta data.

2. Processamento e Limpeza dos Dados:

As informações da API e do CSV são lidas e transformadas para garantir compatibilidade entre as fontes.
A junção dos dados é realizada, onde a chave de correspondência entre os datasets é o código do país.

3. Consolidação Final:

Os dados são mesclados e filtrados para manter apenas as colunas desejadas: codigo, nome, populacao, capital, area, continente e PIB (uma coluna para cada ano de 1960 a 2021).
O resultado é salvo como resultado_final.csv na pasta outputs.

## Execução

Para rodar o projeto, execute o seguinte comando:

   bash
   python src/notebooks/1_coleta_e_cosolidacao_dados.ipynb

Este comando executará todas as etapas descritas acima, desde a coleta de dados até a geração do CSV consolidado.

## Dependências
As dependências do projeto estão listadas no arquivo requirements.txt. As bibliotecas principais incluem:

- requests para requisições HTTP à API.
- pandas para manipulação e junção dos dados.

# Aviso

Este projeto foi desenvolvido como parte de um curso acadêmico na PUCRS e é destinado exclusivamente para fins educacionais. Contribuições externas não são aceitas, para preservar a integridade e originalidade do trabalho.