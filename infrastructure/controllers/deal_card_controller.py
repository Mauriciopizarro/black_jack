from application.deal_card_service import DealCardService
from application.exceptions import IncorrectGameID, GameFinishedError
from domain.game import NotStartedGame, IncorrectPlayerTurn
from domain.user import User
from fastapi import APIRouter, HTTPException, Depends
from infrastructure.authentication.fast_api_authentication import authenticate_with_token

deal_card_service = DealCardService()
router = APIRouter()


@router.post("/deal_card/{game_id}")
async def deal_card_controller(game_id: str, current_user: User = Depends(authenticate_with_token)):
    try:
        deal_card_service.deal_card(current_user.id, game_id)
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game_id entered is finished'
        )
    except IncorrectPlayerTurn:
        raise HTTPException(
            status_code=400, detail='Is not a turn to player entered or id may be incorrect'
        )
    except NotStartedGame:
        raise HTTPException(
            status_code=400, detail='The game is not started',
        )
    return {'message': "Card dealed to player"}
