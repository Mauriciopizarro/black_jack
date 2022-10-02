from fastapi import FastAPI

from controllers import (
    enroll_player_controller,
    start_game_controller,
    status_controller,
    deal_card_controller,
    stand_controller,
    croupier_controller,
    login_controller,
    sign_up_controller,
    create_game_controller
)

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
