from controllers.utils import authenticate_with_token
from models.game import NotStartedGame, IncorrectPlayerTurn
from models.user import User
from services.deal_card_service import DealCardService
from fastapi import APIRouter, HTTPException, Depends
from services.exceptions import GameFinishedError, IncorrectGameID

deal_card_service = DealCardService()
router = APIRouter()


@router.post("/deal_card/{game_id}")
async def deal_card_controller(game_id: int, current_user: User = Depends(authenticate_with_token)):
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
