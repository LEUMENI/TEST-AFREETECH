from flask_sqlalchemy import SQLAlchemy

# Initialisation de la base de données
db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'client'
    
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telephone = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'<Client {self.nom}>'
