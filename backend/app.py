from flask import Flask

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def index():
    return "hi!"