from api_gateway.infrastructure.authentication.local_auth_provider import LocalAuthProvider
from game_service.infrastructure.repositories.game.game_mongo_repository import GameMongoRepository
from api_gateway.infrastructure.repositories.user.user_mongo_repository import UserMongoRepository
from dependency_injector import containers, providers


class Injector(containers.DeclarativeContainer):

    user_repo = providers.Singleton(UserMongoRepository)
    game_repo = providers.Singleton(GameMongoRepository)
    auth_provider = providers.Factory(LocalAuthProvider)


injector = Injector()
injector.wire(modules=["api_gateway.application.login_service", "api_gateway.application.sign_up_service", "api_gateway.application.token_service",
                       "game_service.application.create_game_service", "game_service.application.croupier_service", "game_service.application.deal_card_service",
                       "game_service.application.enroll_player_service", "game_service.application.stand_service", "game_service.application.start_game_service",
                       "game_service.application.status_service"
                       ])
