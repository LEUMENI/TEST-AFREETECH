from flask import render_template, request, redirect, url_for
from app import app  # Importer l'application déjà créée dans app.py
from models import db, Client

@app.route('/')
def index():
    return redirect(url_for('add_client'))  # Redirige vers la route /add_client

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        
        # Créer un nouveau client
        new_client = Client(nom=nom, email=email, telephone=telephone)
        db.session.add(new_client)
        db.session.commit()
        
        return redirect(url_for('index'))  # Redirige vers la page principale
    
    return render_template('add_client.html')  # Rendre le template 'add_client.html'
