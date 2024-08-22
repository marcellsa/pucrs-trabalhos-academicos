class Game:
    def __init__(self, name: str, release_date: str, price: float, developers: list[str], publishers: list[str], 
                 genres: list[str], platforms: dict[str, bool], **kwargs):
        """
        Inicializa uma nova instância da classe Game.

        Parâmetros:
        - name (str): Nome do jogo.
        - release_date (str): Data de lançamento do jogo.
        - price (float): Preço do jogo.
        - developers (list[str]): Lista de desenvolvedores do jogo.
        - publishers (list[str]): Lista de editoras do jogo.
        - genres (list[str]): Lista de gêneros do jogo.
        - platforms (dict[str, bool]): Dicionário indicando a compatibilidade com diferentes plataformas.
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
        """Verifica se o jogo é gratuito."""
        return self.price == 0.0

    def __str__(self) -> str:
        """Retorna uma representação em string do objeto Game."""
        return f"{self.name} ({self.release_date}) - ${self.price:.2f}"

    def __repr__(self) -> str:
        """Retorna uma representação detalhada do objeto Game."""
        return f"Game(name={self.name!r}, release_date={self.release_date!r}, price={self.price!r})"

    def get_platforms(self) -> list[str]:
        """Retorna uma lista das plataformas em que o jogo está disponível."""
        return [platform for platform, available in self.platforms.items() if available]

    def get_developers_string(self) -> str:
        """Retorna os desenvolvedores do jogo como uma string formatada."""
        return ", ".join(self.developers)

    def get_genres_string(self) -> str:
        """Retorna os gêneros do jogo como uma string formatada."""
        return ", ".join(self.genres)

    def get_publishers_string(self) -> str:
        """Retorna as editoras do jogo como uma string formatada."""
        return ", ".join(self.publishers)
