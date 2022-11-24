from fastapi import APIRouter, Depends

from api_gateway.domain.user import User
from api_gateway.infrastructure.authentication.fast_api_authentication import authenticate_with_token
from game_management_service.application.create_game_service import CreateGameService

router = APIRouter()
create_game_service = CreateGameService()


@router.post("/create_game")
async def create_game(current_user: User = Depends(authenticate_with_token)):
    game = create_game_service.create_game(username=current_user.username, user_id=current_user.id)
    return {
        "message": "Game created",
        "id": game.id
    }
