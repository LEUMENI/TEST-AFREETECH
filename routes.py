from flask import render_template, request, redirect, url_for
from app import app
from models import db, Client

@app.route('/')
def index():
    clients = Client.query.all()  # Récupérer tous les clients de la base de données
    return render_template('index.html', clients=clients)

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
        
        return redirect(url_for('index'))  # Rediriger vers la page principale
    
    return render_template('add_client.html')
