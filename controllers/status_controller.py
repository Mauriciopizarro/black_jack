from controllers.utils import ClientErrorResponse
from services.exceptions import NotCreatedGame
from services.status_service import StatusService
from flask.views import View
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import UUID

get_status_service = StatusService()
router = APIRouter()


class Player(BaseModel):
    cards: List[str]
    id: UUID
    is_stand: bool
    name: str
    status: str
    total_points: List[int]


class StatusResponse(BaseModel):
    croupier: Player
    players: List[Player]
    players_quantity: int
    status_game: str


class StatusController(View):
    methods = ['GET']

    def dispatch_request(self):
        try:
            player_status_json = get_status_service.players_status()
            return player_status_json
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='GAME_NOT_CRATED'
            )


@router.get("/player_status", response_model=StatusResponse)
async def get_status_controller():
    try:
        player_status_json = get_status_service.players_status()
        return player_status_json
    except NotCreatedGame:
        raise HTTPException(
            status_code=400, detail='There is not game created'
        )
