from flask import Flask
from models import db
from config import Config

# Créer l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Initialise la base de données
db.init_app(app)

# Créer la base de données si elle n'existe pas
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cette ligne crée les tables automatiquement

    # Importer les routes après avoir initialisé l'app pour éviter les erreurs de dépendance circulaire
    import routes

    app.run(debug=True)
