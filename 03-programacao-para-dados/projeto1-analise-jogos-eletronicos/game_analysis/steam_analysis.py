from typing import List, Dict
from datetime import datetime
from .game import Game

def get_free_vs_paid_percentage(games: List[Game]) -> Dict[str, float]:
    """
    Calcula o percentual de jogos gratuitos e pagos na lista fornecida.

    Parâmetros:
    - games (List[Game]): Lista de objetos Game.

    Retorna:
    - Dict[str, float]: Dicionário com as chaves 'Free' e 'Paid' e seus respectivos percentuais.
    """
    total_games = len(games)
    if total_games == 0:
        return {"Free": 0.0, "Paid": 0.0}

    free_games = sum(1 for game in games if game.is_free())
    paid_games = total_games - free_games

    free_percentage = (free_games / total_games) * 100
    paid_percentage = (paid_games / total_games) * 100

    return {"Free": free_percentage, "Paid": paid_percentage}

def get_year_with_most_games(games: List[Game]) -> List[int]:
    """
    Retorna o(s) ano(s) com o maior número de lançamentos de jogos.

    Parâmetros:
    - games (List[Game]): Lista de objetos Game.

    Retorna:
    - List[int]: Lista dos anos com o maior número de lançamentos.
    """
    year_count = {}
    
    for game in games:
        try:
            year = datetime.strptime(game.release_date, "%Y-%m-%d").year
            if year in year_count:
                year_count[year] += 1
            else:
                year_count[year] = 1
        except ValueError:
            # Ignora datas de lançamento inválidas ou não fornecidas
            continue

    if not year_count:
        return []

    max_games = max(year_count.values())
    most_common_years = [year for year, count in year_count.items() if count == max_games]

    return most_common_years

def get_developer_with_most_games(games: List[Game]) -> str:
    """
    Retorna o desenvolvedor com o maior número de jogos lançados.

    Parâmetros:
    - games (List[Game]): Lista de objetos Game.

    Retorna:
    - str: Nome do desenvolvedor com o maior número de jogos lançados.
    """
    developer_count = {}

    for game in games:
        for developer in game.developers:
            if developer in developer_count:
                developer_count[developer] += 1
            else:
                developer_count[developer] = 1

    if not developer_count:
        return ""

    max_games = max(developer_count.values())
    top_developer = [dev for dev, count in developer_count.items() if count == max_games]

    return top_developer[0] if top_developer else ""
