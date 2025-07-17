import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the db object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'reservations.db')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # Initialize DB with the app
    db.init_app(app)

    # Import and register Blueprints AFTER db is initialized
    from .routes import main
    app.register_blueprint(main)

    # Create DB tables
    with app.app_context():
        db.create_all()

    return app
