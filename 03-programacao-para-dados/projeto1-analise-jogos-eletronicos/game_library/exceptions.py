"""
Este módulo contém definições de exceções personalizadas para o projeto de análise de dados.
"""

class DataLoadError(Exception):
    """
    Exceção levantada quando ocorre um erro ao carregar os dados.
    """
    def __init__(self, message="Erro ao carregar os dados. Verifique o arquivo e tente novamente."):
        self.message = message
        super().__init__(self.message)

class GameNotFoundError(Exception):
    """
    Exceção levantada quando um jogo específico não é encontrado nos dados.
    """
    def __init__(self, game_name, message=None):
        if message is None:
            message = f"O jogo '{game_name}' não foi encontrado."
        self.game_name = game_name
        self.message = message
        super().__init__(self.message)
