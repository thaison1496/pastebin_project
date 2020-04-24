import datetime

from flask import url_for, request, jsonify

from objects import app, db
from models import Pastes

@app.route('/api/hello', methods=['GET'])
def index():
    return "hi!"


@app.route('/api/paste/create_paste', methods=['POST'])
def create_paste():
    params = request.data.decode('utf-8')
    paste = Pastes(content=params, create_date=datetime.datetime.now())
    db.session.add(paste)
    db.session.commit()
    return str(paste)