from flask import Blueprint, request, jsonify
from database.db import db
from flask_bcrypt import Bcrypt
from models.user import User, UserMatch
from flasgger import swag_from

bcrypt = Bcrypt()

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
@swag_from({
    'tags': ['User'],
    'summary': 'Créer un nouvel utilisateur',
    'description': 'Enregistre un nouvel utilisateur avec username, email et password',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'email': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['username', 'email', 'password']
            }
        }
    ],
    'responses': {
        200: {'description': 'Utilisateur créé'},
        400: {'description': 'Erreur'}
    }
})
def register():
    data = request.json
    pw_hash = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    user = User(username=data["username"], email=data["email"], password_hash=pw_hash)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"})

@user_bp.route("/login", methods=["POST"])
@swag_from({
    'tags': ['User'],
    'summary': 'Connexion utilisateur',
    'description': 'Connexion avec email et mot de passe',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        200: {'description': 'Connexion réussie'},
        401: {'description': 'Identifiants invalides'}
    }
})
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and bcrypt.check_password_hash(user.password_hash, data["password"]):
        return jsonify({"id": user.id, "username": user.username, "email": user.email})
    return jsonify({"error": "Invalid credentials"}), 401

@user_bp.route("/matches", methods=["POST"])
@swag_from({
    'tags': ['User'],
    'summary': 'Ajouter un match utilisateur',
    'description': 'Ajoute un match pour un utilisateur',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {'type': 'integer'},
                    'sport': {'type': 'string'},
                    'opponent': {'type': 'string'},
                    'score': {'type': 'string'},
                    'result': {'type': 'string'},
                    'match_date': {'type': 'string', 'format': 'date'}
                },
                'required': ['user_id', 'sport']
            }
        }
    ],
    'responses': {
        200: {'description': 'Match ajouté'}
    }
})
def add_match():
    data = request.json
    match = UserMatch(
        user_id=data["user_id"],
        sport=data["sport"],
        opponent=data.get("opponent"),
        score=data.get("score"),
        result=data.get("result"),
        match_date=data.get("match_date")
    )
    db.session.add(match)
    db.session.commit()
    return jsonify({"message": "Match added"})

@user_bp.route("/matches", methods=["GET"])
@swag_from({
    'tags': ['User'],
    'summary': 'Récupérer les matchs utilisateur',
    'description': 'Récupère la liste des matchs pour un utilisateur donné',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'query',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {'description': 'Liste des matchs'}
    }
})
def get_matches():
    user_id = request.args.get("user_id")
    matches = UserMatch.query.filter_by(user_id=user_id).order_by(UserMatch.match_date.desc()).all()
    return jsonify([{
        "id": m.id,
        "sport": m.sport,
        "opponent": m.opponent,
        "score": m.score,
        "result": m.result,
        "match_date": str(m.match_date)
    } for m in matches])