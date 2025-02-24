from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from instance.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)

    import models.user
    import models.event
    import models.heroes

    from website.routes import register_blueprints
    register_blueprints(app)

    return app