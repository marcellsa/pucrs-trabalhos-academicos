"""
Este módulo define a classe Game, que representa um jogo em uma biblioteca de jogos.
"""
class Game:
    """
    Representa um jogo na plataforma Steam.

    Atributos:
        name (str): Nome do jogo.
        release_date (str): Data de lançamento do jogo.
        price (float): Preço do jogo.
        developers (str): Desenvolvedores do jogo.
    """

    def __init__(self, name, release_date, price, developers):
        """
        Inicializa uma nova instância da classe Game.

        Args:
            name (str): Nome do jogo.
            release_date (str): Data de lançamento do jogo.
            price (float): Preço do jogo.
            developers (str): Desenvolvedores do jogo.
        """
        self.name = name
        self.release_date = release_date
        self.price = price
        self.developers = developers

    def __repr__(self):
        """
        Retorna uma representação textual da instância do jogo.

        Returns:
            str: Representação textual do jogo.
        """
        return f"Game({self.name}, {self.release_date}, ${self.price}, {self.developers})"
