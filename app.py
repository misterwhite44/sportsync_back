from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from config import Config
from database.db import db  # <-- ici
from flask_bcrypt import Bcrypt
from routes.nba_routes import nba_bp
from routes.tennis_routes import tennis_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)  
bcrypt = Bcrypt(app)
swagger = Swagger(app)

with app.app_context():
    db.create_all()

# Blueprints
app.register_blueprint(nba_bp, url_prefix="/api/nba")
app.register_blueprint(tennis_bp, url_prefix="/api/tennis")
app.register_blueprint(user_bp, url_prefix="/api/users")

@app.route("/")
def home():
    return jsonify({"message": "SportSync API running"}), 200

if __name__ == "__main__":
    app.run(debug=True)