from flask import Flask

from controllers.croupier_controller import CroupierPlayController
from controllers.enroll_player_controller import EnrollPlayerController
from controllers.deal_card_controller import DealCardController
from controllers.restart_game_controller import RestartGameController
from controllers.status_controller import StatusController
from controllers.stand_controller import StandController
from controllers.start_game_controller import StartGameController

app = Flask(__name__)
app.add_url_rule('/enroll_player', view_func=EnrollPlayerController.as_view('enroll_player'))
app.add_url_rule('/start_game', view_func=StartGameController.as_view('start_game'))
app.add_url_rule('/player_status', view_func=StatusController.as_view('get_status'))
app.add_url_rule('/deal_card', view_func=DealCardController.as_view('deal_card'))
app.add_url_rule('/stand', view_func=StandController.as_view('stand'))
app.add_url_rule('/croupier_play', view_func=CroupierPlayController.as_view('croupier_play'))
app.add_url_rule('/restart_game', view_func=RestartGameController.as_view('restart_game'))
app.run(debug=True)
