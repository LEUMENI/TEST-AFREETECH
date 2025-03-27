import os

class Config:
    # Configuration de la base de données (SQLite ici)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # Chemin vers la base de données SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactive la surveillance des modifications de la base
    SECRET_KEY = os.urandom(24)  # Clé secrète pour gérer les sessions
