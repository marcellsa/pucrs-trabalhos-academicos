from typing import List, Dict, Tuple
from collections import Counter


class SteamAnalyzer:
    """
    Classe responsável por analisar os dados dos jogos da Steam.
    """

    def __init__(self, games: List[Dict]):
        """
        Inicializa o SteamAnalyzer com a lista de jogos.

        :param games: Lista de dicionários, onde cada dicionário representa um jogo.
        """
        self.games = games

    def calculate_free_paid_percentage(self) -> Tuple[float, float]:
        """
        Calcula o percentual de jogos gratuitos e pagos.

        :return: Uma tupla contendo o percentual de jogos gratuitos e pagos, respectivamente.
        """
        total_games = len(self.games)
        free_games = sum(1 for game in self.games if float(game['Price']) == 0)
        paid_games = total_games - free_games

        free_percentage = (free_games / total_games) * 100
        paid_percentage = (paid_games / total_games) * 100

        return round(free_percentage, 2), round(paid_percentage, 2)

    def find_year_with_most_releases(self) -> List[int]:
        """
        Encontra o(s) ano(s) com o maior número de lançamentos de jogos.

        :return: Uma lista contendo o(s) ano(s) com mais lançamentos.
        """
        year_counter = Counter()

        for game in self.games:
            release_date = game['Release date']
            if release_date:
                year = int(release_date.split('-')[0])
                year_counter[year] += 1

        max_releases = max(year_counter.values())
        return [year for year, releases in year_counter.items() if releases == max_releases]