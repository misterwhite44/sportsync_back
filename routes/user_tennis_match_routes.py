from flask import Blueprint, request, jsonify
from models.user_tennis_match import UserTennisMatch
from database.db import db
from flasgger import swag_from

user_tennis_match_bp = Blueprint("user_tennis_match", __name__)

@user_tennis_match_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['UserTennisMatch'],
    'summary': 'Créer un match de tennis utilisateur',
    'description': 'Crée un match de tennis pour un utilisateur',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {'type': 'integer'},
                    'opponent_name': {'type': 'string'},
                    'match_date': {'type': 'string', 'format': 'date'},
                    'score': {'type': 'string'},
                    'competition': {'type': 'string'},
                    'location': {'type': 'string'}
                },
                'required': ['user_id']
            }
        }
    ],
    'responses': {
        200: {'description': 'Match tennis créé'}
    }
})
def create_tennis_match():
    data = request.json
    match = UserTennisMatch(
        user_id=data["user_id"],
        opponent_name=data.get("opponent_name"),
        match_date=data.get("match_date"),
        score=data.get("score"),
        competition=data.get("competition"),
        location=data.get("location")
    )
    db.session.add(match)
    db.session.commit()
    return jsonify({"message": "Match tennis créé"})

@user_tennis_match_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['UserTennisMatch'],
    'summary': 'Récupérer les matchs tennis',
    'description': 'Récupère tous les matchs tennis',
    'responses': {
        200: {'description': 'Liste des matchs tennis'}
    }
})
def get_tennis_matches():
    matches = UserTennisMatch.query.all()
    return jsonify([
        {
            "id": m.id,
            "user_id": m.user_id,
            "opponent_name": m.opponent_name,
            "match_date": str(m.match_date) if m.match_date else None,
            "score": m.score,
            "competition": m.competition,
            "location": m.location
        } for m in matches
    ])
