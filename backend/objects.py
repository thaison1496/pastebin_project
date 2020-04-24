import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import db_config

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
