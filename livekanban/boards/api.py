from flask import Blueprint, request, jsonify

from livekanban.boards.models import Board
from livekanban.db import scoped_session
from livekanban.utils import json_response

boards_bp = Blueprint('boards', __name__, url_prefix='/boards')

@boards_bp.route("/", methods=['PUT'])
def create_board():
    data = request.get_json()
    
    with scoped_session() as session:
        new_board = Board(name="TO-DO List")
        session.add(new_board)
        
    return json_response(new_board.as_json(), 200)

@boards_bp.errorhandler(404)
@boards_bp.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(error=str(ex)), ex.code
    else:
        return ex