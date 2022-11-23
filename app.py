from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
from auth.auth import auth_bp
from main.main import main_bp
from models.user import User
from db import db, app
from flask_login import LoginManager


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


# app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp)
# app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(main_bp)
# app.register_blueprint(products_bp, url_prefix='/products')
