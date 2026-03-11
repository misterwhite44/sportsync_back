from flask import Blueprint, jsonify
from services.nba_service import get_nba_games

nba_bp = Blueprint("nba", __name__)

@nba_bp.route("/games", methods=["GET"])
def games():
    games = get_nba_games()
    return jsonify(games)