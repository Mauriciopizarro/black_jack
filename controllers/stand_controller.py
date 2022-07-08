
from services.stand_service import StandService
from flask.views import View


stand_service = StandService()


class StandController(View):
    methods = ['POST']

    def dispatch_request(self):
        stand_service.stand()
        return {'message': "Stand"}
