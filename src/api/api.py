from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash
from src.models.user import User
from src.models.kpi import Kpi
from src.models.user_kpi import UserKpi
from src import db

api_bp = Blueprint('api_bp', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='/assets')


@api_bp.route('/api/users/<id>', methods=['GET'])
def get_users(id):
    item = User.query.get(id)
    del item.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)


@api_bp.route('/api/users', methods=['GET'])
def get_user(id):
    users = []
    for user in db.session.query(User).all():
        del user.__dict__['_sa_instance_state']
        users.append(user.__dict__)
    return jsonify(users)


@api_bp.route('/api/user', methods=['POST'])
def create_user():
    body = request.get_json()
    db.session.add(User(body['email'], body['name'], password=generate_password_hash(body['name'], method='sha256')))
    db.session.commit()
    return "user created"


@api_bp.route('/api/kpis/<id>', methods=['GET'])
def get_kpis(id):
    item = User.query.get(id)
    del item.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)


@api_bp.route('/api/kpis', methods=['GET'])
def get_kpi(id):
    kpis = []
    for kpi in db.session.query(Kpi).all():
        del kpi.__dict__['_sa_instance_state']
        kpis.append(kpi.__dict__)
    return jsonify(kpis)
    

@api_bp.route('/api/kpis', methods=['POST'])
def create_kpi():
    body = request.get_json()
    db.session.add(Kpi(body['name'], body['description']))
    db.session.commit()
    return "kpi created"


@api_bp.route('/api/kpis/<id>', methods=['DELETE'])
def delete_kpi(id):
    db.session.query(Kpi).filter_by(id=id).delete()
    db.session.commit()
    return "kpi deleted"



@api_bp.route('/api/user_kpis/<id>', methods=['GET'])
def get_user_kpis(id):
    user_kpi = UserKpi.query.get(id)
    del user_kpi.__dict__['_sa_instance_state']
    return jsonify(user_kpi.__dict__)


@api_bp.route('/api/user_kpis', methods=['GET'])
def get_user_kpi(id):
    user_kpis = []
    for user_kpi in db.session.query(UserKpi).all():
        del user_kpi.__dict__['_sa_instance_state']
        user_kpis.append(user_kpi.__dict__)
    return jsonify(user_kpis)
    

@api_bp.route('/api/user_kpis', methods=['POST'])
def create_user_kpi():
    body = request.get_json()
    db.session.add(UserKpi(body['user_id'], body['kpi_id']))
    db.session.commit()
    return "user kpi link created"


@api_bp.route('/api/user_kpis/<id>', methods=['DELETE'])
def delete_user_kpi(id):
    db.session.query(UserKpi).filter_by(id=id).delete()
    db.session.commit()
    return "user kpi link deleted"
