"""
Módulo responsável por carregar os dados dos jogos da Steam a partir de um arquivo CSV.
"""

import csv
from .exceptions import DataLoadError

def load_data(file_path: str) -> list[dict]:
    """
    Carrega os dados do arquivo CSV e os converte em uma lista de dicionários.
    
    Parâmetros:
    - file_path (str): O caminho para o arquivo CSV.

    Retorna:
    - list[dict]: Uma lista de dicionários, onde cada dicionário representa um jogo.

    Levanta:
    - DataLoadError: Se houver um erro ao carregar os dados.
    """
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except Exception as e:
        raise DataLoadError(f"Erro ao carregar os dados do arquivo {file_path}: {str(e)}") from e

    return data
