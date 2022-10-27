from infrastructure.authentication.local_auth_provider import LocalAuthProvider
from infrastructure.repositories.game.game_pyson_repository import GamePysonRepository
from infrastructure.repositories.user.user_pyson_repository import UserPysonRepository
from dependency_injector import containers, providers


class Injector(containers.DeclarativeContainer):

    user_repo = providers.Singleton(UserPysonRepository)
    game_repo = providers.Singleton(GamePysonRepository)
    auth_provider = providers.Factory(LocalAuthProvider)


injector = Injector()
injector.wire(modules=["application.login_service", "application.sign_up_service", "application.token_service",
                       "application.create_game_service", "application.croupier_service", "application.deal_card_service",
                       "application.enroll_player_service", "application.stand_service", "application.start_game_service",
                       "application.status_service"
                       ])
