# initialize the db and api instance with the flask app
# from ..app import app
from .extensions import db, api, migrate
import os
from dotenv import load_dotenv
from .resources.test import test
from .resources.drinks_api import drinks
from flask import Flask
from .models.drinks_model import Drinks, Drinks_company


def create_app():
    app = Flask(__name__)

    load_dotenv()

    # from the .env file
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DRINKS_URI')

    # get from the container environment
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')

    db.init_app(app)
    api.init_app(app)

    migrate.init_app(app, db, render_as_batch=True)

    # register the blueprint/namespace
    api.add_namespace(test)
    api.add_namespace(drinks)

    return app
