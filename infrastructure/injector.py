from infrastructure.authentication.local_auth_provider import LocalAuthProvider
from infrastructure.repositories.game.game_sql_repository import GameSqlRepository
from infrastructure.repositories.user.user_sql_repository import UserSqlRepository
from dependency_injector import containers, providers


class Injector(containers.DeclarativeContainer):

    user_repo = providers.Singleton(UserSqlRepository)
    game_repo = providers.Singleton(GameSqlRepository)
    auth_provider = providers.Factory(LocalAuthProvider)


injector = Injector()
injector.wire(modules=["application.login_service", "application.sign_up_service", "application.token_service",
                       "application.create_game_service", "application.croupier_service", "application.deal_card_service",
                       "application.enroll_player_service", "application.stand_service", "application.start_game_service",
                       "application.status_service"
                       ])
