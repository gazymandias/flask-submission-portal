# from flask import Flask, request, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
# import os
# from auth.auth import auth_bp
# from main.main import main_bp
# from models.user import User 
# from models.kpi import Kpi
# from models.user_kpi import UserKpi
# from src.db import db, app
# from flask_login import LoginManager
# from sqlalchemy import event

# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=True)

# from werkzeug.security import generate_password_hash
# @event.listens_for(User.__table__, 'after_create')
# def create_users(*args, **kwargs):
#     new_user = User(email='gareth@cadman.com', name='Gareth', password=generate_password_hash('1234', method='sha256'))
#     # add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()

# db.create_all()


# login_manager = LoginManager()
# login_manager.login_view = 'auth_bp.login'
# login_manager.init_app(app)


# @login_manager.user_loader
# def load_user(user_id):
#     # since the user_id is just the primary key of our user table, use it in the query for the user
#     return User.query.get(int(user_id))


# # app.register_blueprint(api_bp, url_prefix='/api')
# app.register_blueprint(auth_bp)
# # app.register_blueprint(cart_bp, url_prefix='/cart')
# app.register_blueprint(main_bp)
# # app.register_blueprint(products_bp, url_prefix='/products')
