"""
Este módulo contém funções para análise de dados de jogos.
"""

from collections import Counter


def get_free_vs_paid_percentage(games):
    """
    Retorna o percentual de jogos gratuitos e pagos na plataforma.

    Args:
        games (list): Lista de objetos Game.

    Returns:
        dict: Dicionário com as chaves 'free' e 'paid' e seus respectivos percentuais.
    """
    total_games = len(games)
    free_games = len([game for game in games if game.price == 0])
    paid_games = total_games - free_games

    return {
        'free': (free_games / total_games) * 100,
        'paid': (paid_games / total_games) * 100
    }

def get_year_with_most_games(games):
    """
    Retorna o ano com o maior número de novos jogos lançados. 
    Em caso de empate, retorna uma lista com os anos empatados.

    Args:
        games (list): Lista de objetos Game.

    Returns:
        int | list: Ano com o maior número de novos jogos ou uma lista de anos em caso de empate.
    """
    release_years = [game.release_date.split('-')[0] for game in games if game.release_date]
    year_count = Counter(release_years)
    max_games = max(year_count.values())
    most_active_years = [year for year, count in year_count.items() if count == max_games]

    if len(most_active_years) == 1:
        return most_active_years[0]
    return most_active_years

def get_developer_with_most_games(games):
    """
    Retorna o desenvolvedor com o maior número de jogos lançados.

    Args:
        games (list): Lista de objetos Game.

    Returns:
        str: Nome do desenvolvedor com o maior número de jogos lançados.
    """
    developers_list = [dev.strip() for game in games for dev in game.
                       developers.split(',') if game.developers]
    developer_count = Counter(developers_list)
    most_common_developer = developer_count.most_common(1)[0][0]

    return most_common_developer
