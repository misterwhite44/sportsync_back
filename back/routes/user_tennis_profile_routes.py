from flask import Blueprint, request, jsonify
from models.user_tennis_profile import UserTennisProfile
from database.db import db
from flasgger import swag_from

user_tennis_profile_bp = Blueprint("user_tennis_profile", __name__)

@user_tennis_profile_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['UserTennisProfile'],
    'summary': 'Créer un profil tennis utilisateur',
    'description': 'Crée un profil tennis pour un utilisateur',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {'type': 'integer'},
                    'fft_id': {'type': 'string'},
                    'ranking': {'type': 'string'},
                    'club': {'type': 'string'}
                },
                'required': ['user_id']
            }
        }
    ],
    'responses': {
        200: {'description': 'Profil tennis créé'}
    }
})
def create_profile():
    data = request.json
    profile = UserTennisProfile(
        user_id=data["user_id"],
        fft_id=data.get("fft_id"),
        ranking=data.get("ranking"),
        club=data.get("club")
    )
    db.session.add(profile)
    db.session.commit()
    return jsonify({"message": "Profil tennis créé"})

@user_tennis_profile_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['UserTennisProfile'],
    'summary': 'Récupérer les profils tennis',
    'description': 'Récupère tous les profils tennis',
    'responses': {
        200: {'description': 'Liste des profils tennis'}
    }
})
def get_profiles():
    profiles = UserTennisProfile.query.all()
    return jsonify([
        {
            "id": p.id,
            "user_id": p.user_id,
            "fft_id": p.fft_id,
            "ranking": p.ranking,
            "club": p.club
        } for p in profiles
    ])
