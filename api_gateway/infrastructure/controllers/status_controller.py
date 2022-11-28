from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from game_service.application.exceptions import IncorrectGameID
from game_service.application.status_service import StatusService

status_service = StatusService()
router = APIRouter()


class Player(BaseModel):
    cards: List[str]
    id: str
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
async def get_status_controller(game_id: str):
    try:
        player_status_json = status_service.players_status(game_id)
        return player_status_json
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
