from fastapi import FastAPI
from pubsub import pub
import shared.injector # no remove this dependecy
from api_gateway.infrastructure.controllers import (
    create_game_controller,
    sign_up_controller,
    start_game_controller,
    deal_card_controller,
    login_controller,
    stand_controller,
    enroll_player_controller,
    status_controller,
    croupier_controller,
)
from game_service.infrastructure.listeners.game_started_listener import create_game

pub.subscribe(create_game, 'game_started')

app = FastAPI()

app.include_router(enroll_player_controller.router)
app.include_router(start_game_controller.router)
app.include_router(status_controller.router)
app.include_router(deal_card_controller.router)
app.include_router(stand_controller.router)
app.include_router(croupier_controller.router)
app.include_router(login_controller.router)
app.include_router(sign_up_controller.router)
app.include_router(create_game_controller.router)
