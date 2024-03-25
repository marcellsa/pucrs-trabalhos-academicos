import csv

meses = {
    1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho',
    7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'
}

def carregar_dados(nome_do_arquivo):
    """
    Carrega os dados de um arquivo CSV para uma lista de dicionários.

    Parâmetros:
    nome_do_arquivo (str): O nome do arquivo CSV a ser carregado.

    Retorna:
    list: Uma lista de dicionários, onde cada dicionário representa uma linha do arquivo CSV.

    Raises:
    FileNotFoundError: Se o arquivo CSV especificado não for encontrado.
    IOError: Se houver um erro ao abrir o arquivo CSV.
    """
    #dados = []
    try:
        with open(nome_do_arquivo, "r", newline="", encoding="utf-8") as arquivo:
            documento = csv.DictReader(arquivo)
            for linha in documento:
                #dados.append(linha)
                return list(documento)
    except FileNotFoundError as e:
        print(f"Erro: Arquivo '{nome_do_arquivo}' não encontrado.")
        raise e
    except IOError as e:
        print(f"Erro: Não foi possível abrir o arquivo '{nome_do_arquivo}'.")
        raise e
    #return dados

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
    # Verifica se o tipo de dados especificado pelo usuário está dentro das opções válidas.
    if tipo_dados not in ["todos", "precipitacao", "temperatura", "umidade_vento"]:
        print("Erro: Tipo de dados inválido.")
        return False
    
    # Verifica se os meses fornecidos estão dentro do intervalo válido de 1 a 12.
    if not 1 <= mes_inicial <= 12 or not 1 <= mes_final <= 12:
        print("Erro: Os meses devem estar entre 1 e 12.")
        return False
    
    # Verifica se os anos fornecidos estão dentro do intervalo válido de 1961 a 2016.
    if ano_inicial < 1961 or ano_final > 2016:
        print("Erro: O ano deve estar entre 1961 e 2016.")
        return False

    # Verifica se o intervalo de datas é válido.
    # O ano inicial não pode ser posterior ao ano final.
    # Se forem iguais, o mês inicial não pode ser posterior ao mês final.
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
    if tipo_dados == "precipitacao":
        # Filtra os dados para incluir apenas as colunas 'data' e 'precip'.
        return [{'data': linha['data'], 'precip': linha['precip']} for linha in dados]
    elif tipo_dados == "temperatura":
        # Filtra os dados para incluir apenas as colunas 'data', 'maxima' e 'minima'.
        return [{'data': linha['data'], 'maxima': linha['maxima'], 'minima': linha['minima'],'horas_insol': linha['horas_insol'], 'temp_media': linha['temp_media']} for linha in dados]
    elif tipo_dados == "umidade_vento":
        # Filtra os dados para incluir apenas as colunas 'data', 'um_relativa' e 'vel_vento'.
        return [{'data': linha['data'], 'um_relativa': linha['um_relativa'], 'vel_vento': linha['vel_vento']} for linha in dados]
    else:
        # Retorna os dados sem filtragem para o tipo "todos".
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
    dados_filtrados_intervalo = filtrar_por_intervalo(dados, mes_inicial, ano_inicial, mes_final, ano_final)
    dados_filtrados_tipo = filtrar_por_tipo(dados_filtrados_intervalo, tipo_dados)
    
    for linha in dados_filtrados_tipo:
        if tipo_dados == "precipitacao":
            print(f"Data: {linha['data']}\tPrecipitação: {linha['precip']}")
        elif tipo_dados == "temperatura":
            print(f"Data: {linha['data']}\tMáxima: {linha['maxima']}\tMínima: {linha['minima']}\tInsolação: {linha['horas_insol']}\tMédia: {linha['temp_media']}")
        elif tipo_dados == "umidade_vento":
            print(f"Data: {linha['data']}\tUmidade: {linha['um_relativa']}\tVel. Vento: {linha['vel_vento']}")
        elif tipo_dados == "todos":
            print(f"Data: {linha['data']}\tPrecipitação: {linha['precip']}\tMáxima: {linha['maxima']}\tMínima: {linha['minima']}\tInsolação: {linha['horas_insol']}\tMédia: {linha['temp_media']}\tUmidade: {linha['um_relativa']}\tVel. Vento: {linha['vel_vento']}")

def mes_mais_chuvoso(dados):
    """
    Encontra o mês mais chuvoso nos dados.

    Parâmetros:
    dados (list): Lista de dicionários contendo os dados meteorológicos.

    Retorna:
    tuple: Uma tupla contendo o ano, mês e a maior precipitação registrada.
    """
    maior_precipitacao = 0
    mes_mais_chuvoso_encontrado = None
    ano_mais_chuvoso = None
    
    for linha in dados:
        precipitacao = float(linha['precip'])
        if precipitacao > maior_precipitacao:
            maior_precipitacao = precipitacao
            mes_mais_chuvoso_encontrado = int(linha['data'].split('/')[1])
            ano_mais_chuvoso = int(linha['data'].split('/')[2])

    return (ano_mais_chuvoso, mes_mais_chuvoso_encontrado, maior_precipitacao)


def calcular_media_minima_mes(dados, numero_mes):
    """
    Calcula a média da temperatura mínima para o mês especificado nos últimos 11 anos.

    Parâmetros:
    dados (list): Lista de dicionários contendo os dados meteorológicos.
    numero_mes (int): O número do mês (1 a 12).

    Retorna:
    dict: Um dicionário onde as chaves são no formato "mesAno" (por exemplo, "novembro2006") e os valores são as médias da temperatura mínima para o mês e ano correspondentes.
    """
    # Validar o número do mês
    if numero_mes < 1 or numero_mes > 12:
        raise ValueError("Número de mês inválido. Por favor, insira um número entre 1 e 12.")

    medias_minimas = {}
    for ano in range(2006, 2017):
        temperaturas_minimas_mes_ano = [float(dado['minima']) for dado in dados if dado['data'].split('/')[2] == str(ano) and dado['data'].split('/')[1] == str(numero_mes).zfill(2)]
        
        # Verificar se há dados disponíveis para o mês e ano especificados
        if temperaturas_minimas_mes_ano:
            media_minima = sum(temperaturas_minimas_mes_ano) / len(temperaturas_minimas_mes_ano)
            nome_mes = meses[numero_mes]
            medias_minimas[f"{nome_mes}{ano}"] = media_minima

    return medias_minimas


def solicitar_tipo_dados():
    """
    Solicita ao usuário para escolher o tipo de dados que deseja visualizar.

    Retorna:
    str: O tipo de dados escolhido.
    """
    print("\nEscolha o tipo de dados que deseja visualizar:")
    print("1 - Todos os dados")
    print("2 - Apenas precipitação")
    print("3 - Apenas temperatura")
    print("4 - Apenas umidade e vento")

    escolha = input("Escolha: ")
    tipos = {"1": "todos", "2": "precipitacao", "3": "temperatura", "4": "umidade_vento"}
    
    if escolha in tipos:
        return tipos[escolha]
    else:
        print("Escolha inválida.")
        return solicitar_tipo_dados()

def main():
    # Carregar dados
    nome_do_arquivo = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"
    dados_carregados = carregar_dados(nome_do_arquivo)

    # Solicitar entrada do usuário
    mes_inicial = int(input("Digite o mês inicial (1 a 12): "))
    ano_inicial = int(input("Digite o ano inicial (1961 a 2016): "))
    mes_final = int(input("Digite o mês final (1 a 12): "))
    ano_final = int(input("Digite o ano final (1961 a 2016): "))
    tipo_dados = solicitar_tipo_dados()

    # Visualizar dados
    visualizar_dados(dados_carregados, mes_inicial, ano_inicial, mes_final, ano_final, tipo_dados)

    # Encontrar o mês mais chuvoso
    ano_chuvoso, mes_chuvoso, precipitacao = mes_mais_chuvoso(dados_carregados)
    print("\nMês mais chuvoso:")
    print(f"> O mês mais chuvoso foi {mes_chuvoso}/{ano_chuvoso} com precipitação de {precipitacao} mm.")

    # Calcular média da temperatura mínima para um determinado mês
    numero_mes = int(input("\nDigite o número do mês (1-12): "))
    if numero_mes < 1 or numero_mes > 12:
        print("Número de mês inválido. Por favor, insira um número entre 1 e 12.")
        return

    try:
        medias_minimas_mes = calcular_media_minima_mes(dados_carregados, numero_mes)
        media_geral = sum(medias_minimas_mes.values()) / len(medias_minimas_mes)
        print(f"Média da temperatura mínima do mês {meses[numero_mes]} nos últimos 11 anos (2006 a 2016)")
        for chave, valor in medias_minimas_mes.items():
            print(f"> Média mínima de {chave}: {valor:.2f}°C")
        print(f"\nMédia geral da temperatura mínima do mês {meses[numero_mes]} nos últimos 11 anos (2006 a 2016):")
        print(f"> Média geral da temperatura mínima para o mês: {media_geral:.2f}°C\n")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
