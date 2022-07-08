
from services.croupier_service import CroupierService
from flask.views import View

croupier_service = CroupierService()


class CroupierPlayController(View):
    methods = ['POST']

    def dispatch_request(self):
        croupier_service.croupier_play()
        return {'message': "Croupier is playing"}
