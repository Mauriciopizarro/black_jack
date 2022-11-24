from abc import ABC, abstractmethod
from game_management_service.domain.game import Game


class GameRepository(ABC):

    @abstractmethod
    def save(self, game: Game) -> Game:
        pass

    @abstractmethod
    def get(self, game_id: int) -> Game:
        pass

    @abstractmethod
    def update(self, game: Game) -> Game:
        pass
