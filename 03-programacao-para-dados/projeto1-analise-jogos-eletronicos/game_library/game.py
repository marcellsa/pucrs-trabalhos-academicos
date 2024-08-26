"""
Este módulo define a classe Game, que representa um jogo em uma biblioteca de jogos.

A classe Game inclui atributos como nome, data de lançamento, preço, desenvolvedores,
editoras, gêneros e plataformas. Além disso, fornece métodos para verificar se o jogo
é gratuito, obter plataformas disponíveis e formatar informações sobre desenvolvedores,
gêneros e editoras como strings.

Classe:
- Game: Representa um jogo e fornece métodos para acessar e formatar informações
  sobre ele.
"""

class Game:
    """
    Representa um jogo em uma biblioteca de jogos.

    Atributos:
    - name (str): Nome do jogo.
    - release_date (str): Data de lançamento do jogo.
    - price (float): Preço do jogo.
    - developers (list[str]): Lista de desenvolvedores do jogo.
    - publishers (list[str]): Lista de editoras do jogo.
    - genres (list[str]): Lista de gêneros do jogo.
    - platforms (dict[str, bool]): Dicionário indicando plataformas comnpatíveis.
    - additional_info (dict): Outros atributos adicionais do jogo.

    Métodos:
    - is_free(): Verifica se o jogo é gratuito.
    - get_platforms(): Retorna uma lista das plataformas em que o jogo está disponível.
    - get_developers_string(): Retorna os desenvolvedores do jogo como uma string formatada.
    - get_genres_string(): Retorna os gêneros do jogo como uma string formatada.
    - get_publishers_string(): Retorna as editoras do jogo como uma string formatada.
    """

    def __init__(self, name: str, release_date: str, price: float, developers: list[str], 
                 publishers: list[str], genres: list[str], platforms: dict[str, bool], **kwargs):
        """
        Inicializa uma nova instância da classe Game.

        Parâmetros:
        - name (str): Nome do jogo.
        - release_date (str): Data de lançamento do jogo.
        - price (float): Preço do jogo.
        - developers (list[str]): Lista de desenvolvedores do jogo.
        - publishers (list[str]): Lista de editoras do jogo.
        - genres (list[str]): Lista de gêneros do jogo.
        - platforms (dict[str, bool]): Dicionário indicando plataformas compatíveis.
        - **kwargs: Outros atributos do jogo que podem ser armazenados como propriedades adicionais.
        """
        self.name = name
        self.release_date = release_date
        self.price = price
        self.developers = developers
        self.publishers = publishers
        self.genres = genres
        self.platforms = platforms
        self.additional_info = kwargs

    def is_free(self) -> bool:
        """
        Verifica se o jogo é gratuito.
        """
        return self.price == 0.0

    def __str__(self) -> str:
        """
        Retorna uma representação em string do objeto Game.
        """
        return f"{self.name} ({self.release_date}) - ${self.price:.2f}"

    def __repr__(self) -> str:
        """
        Retorna uma representação detalhada do objeto Game.
        """
        return f"Game(name={self.name!r}, release_date={self.release_date!r}, price={self.price!r})"

    def get_platforms(self) -> list[str]:
        """
        Retorna uma lista das plataformas em que o jogo está disponível.
        """
        return [platform for platform, available in self.platforms.items() if available]

    def get_developers_string(self) -> str:
        """
        Retorna os desenvolvedores do jogo como uma string formatada.
        """
        return ", ".join(self.developers)

    def get_genres_string(self) -> str:
        """
        Retorna os gêneros do jogo como uma string formatada.
        """
        return ", ".join(self.genres)

    def get_publishers_string(self) -> str:
        """
        Retorna as editoras do jogo como uma string formatada.
        """
        return ", ".join(self.publishers)
