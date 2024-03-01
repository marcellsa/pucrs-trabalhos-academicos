def validar_temperatura(temperatura):
    """
    Valida a temperatura inserida pelo usuário.
    
    Parêmntro:
        temperatura (str): A temperatura inserida pelo usuário.
        
    Retorno:
        float or None: A temperatura validada ou None se a entrada for inválida.
    """
    while True:
        try:
            temperatura = float(temperatura)
            if -60 <= temperatura <= 50:
                return temperatura
            else:
                print("Por favor, informe uma temperatura no intervalo de -60 graus à +50 graus.")
                return None
        except ValueError:
            print("Por favor, informe uma temperatura válida!")
            return None

def obter_dados_mensais(meses):
    """
    Obtém as temperaturas máximas mensais inseridas pelo usuário.
    
    Parêmntro:
        meses (dict): Um dicionário contendo os números dos meses como chaves e os nomes dos meses como valores.
        
    Retorno:
        list: Uma lista contendo as temperaturas máximas inseridas pelo usuário para cada mês.
    """
    temperaturas = []
    for i in range(1, 13):
        temperatura_maxima = None
        while temperatura_maxima is None:
            print(f"\nInforme os dados para {meses[i]}: ")
            temperatura_maxima = validar_temperatura(input(">Temperatura máxima do mês (em ºC): "))
        temperaturas.append(temperatura_maxima)
    return temperaturas

def exibir_titulo_do_programa():
    print("""
▄▀█ █▄░█ ▄▀█ █░░ █ █▀ █▀▀   █▀▄▀█ █▀▀ ▀█▀ █▀▀ █▀█ █▀█ █▀█ █░░ █▀█ █▀▀ █ █▀▀ ▄▀█
█▀█ █░▀█ █▀█ █▄▄ █ ▄█ ██▄   █░▀░█ ██▄ ░█░ ██▄ █▄█ █▀▄ █▄█ █▄▄ █▄█ █▄█ █ █▄▄ █▀█
        """)

def main():
    # Dicionário contendo os números dos meses como chaves e os nomes dos meses como valores
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    exibir_titulo_do_programa()
    # Obter as temperaturas máximas mensais inseridas pelo usuário
    temperaturas = obter_dados_mensais(meses)

    # Calcular a temperatura média máxima anual
    media_anual = sum(temperaturas) / len(temperaturas)
    # Contar a quantidade de meses escaldantes (temperatura > 33ºC)
    meses_escaldantes = sum(1 for temperatura in temperaturas if temperatura > 33)
    # Determinar o mês mais escaldante do ano
    mes_mais_escaldante = meses[temperaturas.index(max(temperaturas)) + 1]
    # Determinar o mês menos quente do ano
    mes_menos_escaldante = meses[temperaturas.index(min(temperaturas)) + 1]


    # Exibir os resultados
    exibir_titulo_do_programa()
    print("\n[Dᴀᴅᴏs Esᴛᴀᴛɪ́sᴛɪᴄᴏs] --------------------")
    print(f"- Temperatura média máxima anual: {media_anual:.2f}ºC")
    print(f"- Quantidade de meses escaldantes: {meses_escaldantes}")
    print(f"- Mês mais escaldante do ano: {mes_mais_escaldante.title()}")
    print(f"- Mês menos quente do ano: {mes_menos_escaldante.title()}\n")

if __name__ == "__main__":
    main()
