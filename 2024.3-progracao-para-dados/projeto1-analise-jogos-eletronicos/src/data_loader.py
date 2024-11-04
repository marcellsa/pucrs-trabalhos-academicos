import csv
from typing import List, Dict


class DataLoader:
    """
    Classe responsável por carregar e processar dados de jogos da Steam.
    """

    def __init__(self, file_path: str):
        """
        Inicializa o SteamDataLoader com o caminho do arquivo CSV.

        :param file_path: Caminho para o arquivo CSV contendo os dados dos jogos.
        """
        self.file_path = file_path
        self.data = []

    def load_data(self) -> None:
        """
        Carrega os dados do arquivo CSV para a memória.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            self.data = list(csv_reader)

    def get_games(self) -> List[Dict]:
        """
        Retorna a lista de jogos carregados.

        :return: Lista de dicionários, onde cada dicionário representa um jogo.
        """
        return self.data
