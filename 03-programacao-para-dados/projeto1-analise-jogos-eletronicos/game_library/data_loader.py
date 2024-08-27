"""
Módulo responsável por carregar os dados dos jogos da Steam a partir de um arquivo CSV.
"""

import csv
from .exceptions import DataLoadError

def load_data(filepath):
    """
    Carrega os dados do arquivo CSV especificado e retorna uma lista de dicionários.
    """
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        return data
    except Exception as e:
        raise DataLoadError(f"Erro ao carregar dados: {e}") from e
