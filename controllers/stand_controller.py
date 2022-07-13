from controllers.utils import ClientErrorResponse
from services.stand_service import StandService, NoTurnsToStand
from flask.views import View


stand_service = StandService()


class StandController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            stand_service.stand()
        except NoTurnsToStand:
            return ClientErrorResponse(
                description='There arent turns to stand',
                code='NOT_TURNS_TO_STAND',
            )
        return {'message': "Stand"}
