from flask import Flask
from config import config

#database
from database.Database import db

#routes
from .routes import ContactsRoutes

def init_app(configname):

    app = Flask(__name__)

    #Configuration
    app.config.from_object(config[configname])

    db.init_app(app)

    #Blueprints
    app.register_blueprint(ContactsRoutes.main, url_prefix='/contactos_blueprint')

    return app