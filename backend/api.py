from flask import url_for, request, jsonify

from app import app
from models import Paste

@app.route('/api/hello', methods=['GET'])
def index():
    return "hi!"


@app.route('/api/paste/create_paste', methods=['POST'])
def create_paste():
    params = request.data.decode('utf-8')
    return params