import csv

def carregar_dados(nome_do_arquivo):
    """
    Carrega os dados de um arquivo CSV para uma lista de dicionários.

    Parâmetros:
    nome_do_arquivo (str): O nome do arquivo CSV a ser carregado.

    Retorna:
    list: Uma lista de dicionários, onde cada dicionário representa uma linha do arquivo CSV.
    """
    dados = []
    try:
        with open(nome_do_arquivo, "r", newline="") as arquivo:
            documento = csv.DictReader(arquivo)
            for linha in documento:
                dados.append(linha)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_do_arquivo}' não encontrado.")
    except IOError:
        print(f"Erro: Não foi possível abrir o arquivo '{nome_do_arquivo}'.")
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
    return dados

def validar_entradas(mes_inicial, ano_inicial, mes_final, ano_final, tipo_dados):
    """
    Valida os dados de entrada fornecidos pelo usuário.

    Parâmetros:
    mes_inicial (int): Mês inicial do intervalo.
    ano_inicial (int): Ano inicial do intervalo.
    mes_final (int): Mês final do intervalo.
    ano_final (int): Ano final do intervalo.
    tipo_dados (str): Tipo de dados a serem visualizados: "todos", "precipitacao", "temperatura" ou "umidade_vento".

    Retorna:
    bool: True se os dados de entrada forem válidos, False caso contrário.
    """
    if tipo_dados not in ["todos", "precipitacao", "temperatura", "umidade_vento"]:
        print("Erro: Tipo de dados inválido.")
        return False
    if not(1 <= mes_inicial <= 12) or not(1 <= mes_final <= 12):
        print("Erro: Os meses devem estar entre 1 e 12.")
        return False
    if ano_inicial < 1961 or ano_final > 2016:
        print("Erro: O ano deve estar entre 1961 e 2016.")
        return False
    if (ano_inicial > ano_final) or (ano_inicial == ano_final and mes_inicial > mes_final):
        print("Erro: Intervalo de datas inválido.")
        return False
    return True

def filtrar_por_tipo(dados, tipo_dados):
    """
    Filtra os dados de acordo com o tipo selecionado.

    Parâmetros:
    dados (list): Lista de dicionários contendo os dados meteorológicos.
    tipo_dados (str): Tipo de dados a serem visualizados: "todos", "precipitacao", "temperatura" ou "umidade_vento".

    Retorna:
    list: Lista filtrada de dicionários contendo os dados meteorológicos.
    """
    if tipo_dados == "2":
        return [linha for linha in dados if float(linha['precip'])]
    elif tipo_dados == "3":
        return [linha for linha in dados if float(linha['maxima']) or float(linha['minima'])]
    elif tipo_dados == "4":
        return [linha for linha in dados if float(linha['um_relativa']) or float(linha['vel_vento'])]
    else:
        return dados

def filtrar_por_intervalo(dados, mes_inicial, ano_inicial, mes_final, ano_final):
    """
    Filtra os dados pelo intervalo especificado.

    Parâmetros:
    dados (list): Lista de dicionários contendo os dados meteorológicos.
    mes_inicial (int): Mês inicial do intervalo.
    ano_inicial (int): Ano inicial do intervalo.
    mes_final (int): Mês final do intervalo.
    ano_final (int): Ano final do intervalo.

    Retorna:
    list: Lista filtrada de dicionários contendo os dados meteorológicos.
    """
    return [linha for linha in dados if
            (ano_inicial, mes_inicial) <= (int(linha['data'].split('/')[2]), int(linha['data'].split('/')[1])) <= (ano_final, mes_final)]


def visualizar_dados(dados, mes_inicial, ano_inicial, mes_final, ano_final, tipo_dados):
    """
    Visualiza os dados dentro de um intervalo especificado pelo usuário.

    Parâmetros:
    dados (list): Lista de dicionários contendo os dados meteorológicos.
    mes_inicial (int): Mês inicial do intervalo.
    ano_inicial (int): Ano inicial do intervalo.
    mes_final (int): Mês final do intervalo.
    ano_final (int): Ano final do intervalo.
    tipo_dados (str): Tipo de dados a serem visualizados: "todos", "precipitacao", "temperatura" ou "umidade_vento".
    """
    if not validar_entradas(mes_inicial, ano_inicial, mes_final, ano_final, tipo_dados):
        return
    
    dados_filtrados = filtrar_por_tipo(dados, tipo_dados)
    dados_filtrados = filtrar_por_intervalo(dados_filtrados, mes_inicial, ano_inicial, mes_final, ano_final)

    if dados_filtrados:
        for linha in dados_filtrados:
            print(f"Data: {linha['data']}\tPrecipitação: {linha['precip']}\tMáxima: {linha['maxima']}\tMínima: {linha['minima']}\tInsolação: {linha['horas_insol']}\tMédia: {linha['temp_media']}\tUmidade: {linha['um_relativa']}\tVel. Vento: {linha['vel_vento']}")
    else:
        print("Nenhum dado encontrado para o intervalo e tipo de dados especificados.")


def exibir_dados(dados_carregados, n):
    """
    Exibe os primeiros N registros dos dados.

    Parâmetros:
    dados (list): Uma lista de dicionários contendo os dados a serem exibidos.
    n (int): O número de registros a serem exibidos.

    Retorna:
    None
    """
    for i in range(min(n, len(dados_carregados))):
        print(dados_carregados[i])

def main():
    mes_inicial = int(input("Digite o mês inicial (1 a 12): "))
    ano_inicial = int(input("Digite o ano inicial (1961 a 2016): "))
    mes_final = int(input("Digite o mês final (1 a 12): "))
    ano_final = int(input("Digite o ano final (1961 a 2016): "))
    tipo_dados = int(input("Digite o tipo de dados que deseja visualizar:\n"
                           "1 - Todos os dados\n"
                           "2 - Apenas precipitação\n"
                           "3 - Apenas temperatura\n"
                           "4 - Apenas umidade e vento\n"
                           "Escolha: "))
    
    if tipo_dados == 1:
        tipo_dados = "todos"
    elif tipo_dados == 2:
        tipo_dados = "precipitacao"
    elif tipo_dados == 3:
        tipo_dados = "temperatura"
    elif tipo_dados == 4:
        tipo_dados = "umidade_vento"
    else:
        print("Escolha inválida.")
        return
    
    nomo_do_arquivo = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"
    dados_carregados = carregar_dados(nomo_do_arquivo)
    #exibir_dados(dados_carregados, 10)
    visualizar_dados(dados_carregados, mes_inicial, ano_inicial, mes_final, ano_final, tipo_dados)


if __name__ == "__main__":
    main()
