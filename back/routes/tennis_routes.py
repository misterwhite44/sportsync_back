from flask import Blueprint, jsonify, request
from services.tennis_service import get_player_rankings, get_upcoming_matches, get_previous_matches, get_calendar

tennis_bp = Blueprint("tennis", __name__)

@tennis_bp.route("/rankings", methods=["GET"])
def rankings():
    data = get_player_rankings()
    return jsonify(data)

@tennis_bp.route("/upcoming-matches", methods=["GET"])
def upcoming_matches_route():
    data = get_upcoming_matches()
    return jsonify(data)

@tennis_bp.route("/previous-matches", methods=["GET"])
def previous_matches_route():
    data = get_previous_matches()
    return jsonify(data)

@tennis_bp.route("/calendar", methods=["GET"])
def calendar_route():
    month = request.args.get("month")
    year = request.args.get("year")
    data = get_calendar(month, year)
    return jsonify(data)