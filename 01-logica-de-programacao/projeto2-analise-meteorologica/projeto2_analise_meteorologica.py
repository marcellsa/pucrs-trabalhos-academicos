import csv

def carregar_dados(nome_do_arquivo):
    """
    Carrega os dados de um arquivo CSV para uma lista de dicionários.

    Parâmetros:
    nomo_do_arquivo (str): O nome do arquivo CSV a ser carregado.

    Retorna:
    list: Uma lista de dicionários, onde cada dicionário representa uma linha do arquivo CSV.
    """
    dados = []
    with open(nome_do_arquivo, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            dados.append(linha)
    return dados

def exibir_dados(dados, n):
    """
    Exibe os primeiros N registros dos dados.

    Parâmetros:
    dados (list): Uma lista de dicionários contendo os dados a serem exibidos.
    n (int): O número de registros a serem exibidos.

    Retorna:
    None
    """
    for i in range(min(n, len(dados))):
        print(dados[i])


nomo_do_arquivo = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"
dados = carregar_dados(nomo_do_arquivo)
exibir_dados(dados, 10)
