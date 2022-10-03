from models.game import NotStartedGame
from services.exceptions import NotCreatedGame
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


@router.get("/player_status", response_model=StatusResponse)
async def get_status_controller():
    try:
        player_status_json = get_status_service.players_status()
        return player_status_json
    except NotCreatedGame:
        raise HTTPException(
            status_code=400, detail='There is not game created'
        )
    except NotStartedGame:
        raise HTTPException(
            status_code=400, detail='The game is not started',
        )
