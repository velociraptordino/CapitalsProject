from flask import render_template

from app import app
from app.model import Player
from app.sortPlayers import getPlayers

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', players=Player.query.all())

@app.route('/partb')
def sorted():
    return render_template('partb.html', sortedPlayers=getPlayers())
