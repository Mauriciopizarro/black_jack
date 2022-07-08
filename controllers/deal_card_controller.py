
from services.deal_card_service import DealCardService
from flask.views import View

deal_card_service = DealCardService()


class DealCardController(View):
    methods = ['POST']

    def dispatch_request(self):
        deal_card_service.deal_card()
        return {'message': "Card deal!"}
