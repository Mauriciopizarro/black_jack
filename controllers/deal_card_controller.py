from controllers.utils import authenticate_with_token
from models.game import NotStartedGame
from models.user import User
from services.deal_card_service import DealCardService, NotPlayerTurn, CroupierTurn, IncorrectPlayerTurn, EmptyPlayerID
from fastapi import APIRouter, HTTPException, Depends
from services.exceptions import NotCreatedGame, GameFinishedError


deal_card_service = DealCardService()
router = APIRouter()


@router.post("/deal_card")
async def deal_card_controller(current_user: User = Depends(authenticate_with_token)):
    try:
        deal_card_service.deal_card(current_user.user_id)
    except NotCreatedGame:
        raise HTTPException(
            status_code=400, detail='There is not game created',
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game is finished'
        )
    except NotPlayerTurn:
        raise HTTPException(
            status_code=400, detail='Is not player turn'
        )
    except CroupierTurn:
        raise HTTPException(
            status_code=400, detail='Is turn to croupier'
        )
    except IncorrectPlayerTurn:
        raise HTTPException(
            status_code=400, detail='Is not a turn to player entered or id may be incorrect'
        )
    except EmptyPlayerID:
        raise HTTPException(
            status_code=400, detail='To use this resource is necessary to enter the player_id'
        )
    except NotStartedGame:
        raise HTTPException(
            status_code=400, detail='The game is not started',
        )
    return {'message': "Card dealed to player"}
