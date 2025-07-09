from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'this-should-be-changed'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
