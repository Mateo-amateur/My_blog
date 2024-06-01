from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'asdfg'
)

from app import routes