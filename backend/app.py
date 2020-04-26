import datetime
import json

from flask import url_for, request, jsonify, abort

from objects import app, db
from models import Pastes
import utils

@app.route('/api/hello', methods=['GET'])
def index():
    return "hi!"


@app.route('/api/paste/create_paste', methods=['POST'])
def create_paste():
    params = request.data.decode('utf-8')
    paste = Pastes(
            content=params,
            paste_id=utils.generate_random_paste_id(),
            create_date=datetime.datetime.now())
    db.session.add(paste)
    db.session.commit()
    return str(paste)


@app.route('/api/paste/<paste_id>', methods=['GET'])
def get_paste(paste_id: str):
    results = Pastes.query.filter(Pastes.paste_id==paste_id).all()
    if len(results) == 0:
        abort(404)
    return results[0].content


@app.route('/api/paste/list', methods=['GET'])
def list_pastes():
    rows = Pastes.query.all()
    result = ([
                [row.paste_id,
                utils.shorten_paste_content(row.content),
                row.create_date.strftime("%Y-%m-%d %H:%M:%S")]
            for row in rows])
    return json.dumps(result)
