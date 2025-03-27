from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Créer l'application Flask
app = Flask(__name__)

# Configurer la base de données (utilisation de SQLite dans ce cas)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialiser SQLAlchemy
db = SQLAlchemy(app)

# Définir le modèle Client
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telephone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Client {self.nom}>'

# Créer la base de données si elle n'existe pas
with app.app_context():
    db.create_all()  # Crée les tables automatiquement

# Route pour afficher le formulaire d'ajout d'un client
@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        
        # Créer un nouveau client
        new_client = Client(nom=nom, email=email, telephone=telephone)
        db.session.add(new_client)
        db.session.commit()

        return redirect(url_for('index'))  # Rediriger vers la page principale (index)
    
    return render_template('add_client.html')  # Rendre le template 'add_client.html'

# Route pour afficher la liste des clients
@app.route('/')
def index():
    clients = Client.query.all()  # Récupérer tous les clients de la base de données
    return render_template('index.html', clients=clients)

# Exécuter l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
