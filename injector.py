from repositories.game.game_pyson_repository import GamePysonRepository
from repositories.user.user_pyson_repository import UserPysonRepository
from dependency_injector import containers, providers


class Injector(containers.DeclarativeContainer):

    user_repo = providers.Factory(UserPysonRepository)
    game_repo = providers.Singleton(GamePysonRepository)


injector = Injector()
injector.wire(modules=["services.login_service", "services.sign_up_service", "services.token_service",
                       "services.create_game_service", "services.croupier_service", "services.deal_card_service",
                       "services.enroll_player_service", "services.stand_service", "services.start_game_service",
                       "services.status_service"
                       ])
