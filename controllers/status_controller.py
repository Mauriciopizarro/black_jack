from models.game import NotStartedGame
from services.exceptions import IncorrectGameID
from services.status_service import StatusService
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

get_status_service = StatusService()
router = APIRouter()


class Player(BaseModel):
    cards: List[str]
    id: int
    is_stand: bool
    name: str
    status: str
    total_points: List[int]


class Croupier(BaseModel):
    cards: List[str]
    is_stand: bool
    name: str
    status: str
    total_points: List[int]


class StatusResponse(BaseModel):
    croupier: Croupier
    players: List[Player]
    players_quantity: int
    status_game: str


@router.get("/player_status/{game_id}", response_model=StatusResponse)
async def get_status_controller(game_id: int):
    try:
        player_status_json = get_status_service.players_status(game_id)
        return player_status_json
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
    except NotStartedGame:
        raise HTTPException(
            status_code=400, detail='The game is not started',
        )
