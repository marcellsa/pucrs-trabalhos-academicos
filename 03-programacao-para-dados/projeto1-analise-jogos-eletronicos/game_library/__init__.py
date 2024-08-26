"""
Módulo de inicialização para o pacote 'game_library'.

Este módulo configura o pacote 'game_library' para fornecer as funcionalidades
de carregamento de dados, manipulação de jogos e análise de dados dos jogos.
"""

# Importações de inicialização do pacote, se necessário
from .data_loader import load_data
from .game import Game
from .exceptions import DataLoadError, GameNotFoundError
from .steam_analysis import (
    get_free_vs_paid_percentage,
    get_year_with_most_games,
    get_developer_with_most_games
)
