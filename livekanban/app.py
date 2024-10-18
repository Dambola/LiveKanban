from flask import Flask, Blueprint, render_template, make_response
from livekanban.db import Base, Engine

import livekanban.boards
import livekanban.states
import livekanban.tasks

app = Flask(__name__)
Base.metadata.create_all(Engine)

# BEGIN: API Registration

api_bp = Blueprint('api', __name__, url_prefix='/api')

from livekanban.boards.api import boards_bp
api_bp.register_blueprint(boards_bp)

app.register_blueprint(api_bp)

# END: API Registration

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/update/<board_id>")
def update_board(board_id):
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 200, headers)
