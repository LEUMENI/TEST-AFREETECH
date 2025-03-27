# Projet INTIA Assurance - Plateforme de Gestion des Clients et des assurances 

## Description

Ce projet consiste en une plateforme de gestion des clients et les assurances pour la société INTIA Assurance. L'application permet l'ajout, la modification, la suppression et la consultation des informations clients et lles assurances. Elle utilise Flask comme framework backend, avec une base de données SQLite pour stocker les informations.

## Prérequis

- **Python 3.7+**
- **pip** (pour installer les dépendances)
- **Git** (pour cloner le dépôt)
- **Flask** (framework backend)
- **SQLite** (base de données intégrée)

## Procédure d'Installation

### 1. Cloner le Dépôt

Commence par cloner ce dépôt dans ton environnement local.

```bash
git clone https://github.com/LEUMENI/TEST-AFREETECH.git
cd TEST-AFREETECH

2.  Créer un Environnement Virtuel

Il est recommandé de créer un environnement virtuel pour gérer les dépendances Python.
python -m venv venv
3.  Activer l'Environnement Virtuel

Sur Windows :
venv\Scripts\activate
4. Installer les Dépendances

pip install -r requirements.txt
5. Configurer la Base de Données

Une fois les dépendances installées, la base de données SQLite sera automatiquement créée au premier lancement de l'application. Flask utilise SQLAlchemy pour gérer les opérations de base de données.
6. Lancer l'Application

python app.py
7. Accéder à l'Application

Ouvre un navigateur web et accède à l'URL suivante :
http://127.0.0.1:5000
