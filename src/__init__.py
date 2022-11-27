"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database setup
db = SQLAlchemy()

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('src.config.Config')  # configure app using the Config class defined in src/config.py

    db.init_app(app)  # initialise the database for the app

    with app.app_context():
        from src.models.kpi import Kpi
        from src.models.user_kpi import UserKpi
        from src.models.kpi_data import KpiData
        from src.models.user import User # this import allows us to create the table if it does not exist
        db.create_all()

        from flask_login import LoginManager
        login_manager = LoginManager()
        login_manager.login_view = 'auth_bp.login'
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(user_id):
            # since the user_id is just the primary key of our user table, use it in the query for the user
            return User.query.get(int(user_id))

        from src.auth.auth import auth_bp
        from src.main.main import main_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(main_bp)
        from src.api.api import api_bp
        app.register_blueprint(api_bp)
        return app