from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash
from src.models.user import User
from src.models.kpi import Kpi
from src.models.user_kpi import UserKpi
from src.models.kpi_data import KpiData
from src import db
from sqlalchemy.exc import SQLAlchemyError

api_bp = Blueprint('api_bp', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='/assets')


@api_bp.route('/api/users/<id>', methods=['GET'])
def get_users(id):
    try:
        user = User.query.get(id)
        del user.__dict__['_sa_instance_state']
        return jsonify(user.__dict__)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/users', methods=['GET'])
def get_user():
    try:
        users = []
        for user in db.session.query(User).all():
            del user.__dict__['_sa_instance_state']
            users.append(user.__dict__)
        return jsonify(users)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/user', methods=['POST'])
def create_user():
    try:
        body = request.get_json()
        new_user = User(email=body['email'], name=body['name'], password=generate_password_hash(body['password'], method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return "user created"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/kpis/<id>', methods=['GET'])
def get_kpi(id):
    try:
        kpi = User.query.get(id)
        del kpi.__dict__['_sa_instance_state']
        return jsonify(kpi.__dict__)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/kpis', methods=['GET'])
def get_kpis():
    try:
        kpis = []
        for kpi in db.session.query(Kpi).all():
            del kpi.__dict__['_sa_instance_state']
            kpis.append(kpi.__dict__)
        return jsonify(kpis)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error
    

@api_bp.route('/api/kpis', methods=['POST'])
def create_kpi():
    try:
        body = request.get_json()
        new_kpi = Kpi(name=body['name'], description=body['description'])
        db.session.add(new_kpi)
        db.session.commit()
        return "kpi created"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/kpis/<id>', methods=['DELETE'])
def delete_kpi(id):
    try:
        db.session.query(Kpi).filter_by(id=id).delete()
        db.session.commit()
        return "kpi deleted"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/user_kpis/<id>', methods=['GET'])
def get_user_kpi(id):
    try:
        user_kpi = UserKpi.query.get(id)
        del user_kpi.__dict__['_sa_instance_state']
        return jsonify(user_kpi.__dict__)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error

@api_bp.route('/api/user_kpis', methods=['GET'])
def get_user_kpis():
    try:
        user_kpis = []
        for user_kpi in db.session.query(UserKpi).all():
            del user_kpi.__dict__['_sa_instance_state']
            user_kpis.append(user_kpi.__dict__)
        return jsonify(user_kpis)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error
    

@api_bp.route('/api/user_kpis', methods=['POST'])
def create_user_kpi():
    try:
        body = request.get_json()
        new_kpi = UserKpi(user_id=body['user_id'], kpi_id=body['kpi_id'])
        db.session.add(new_kpi)
        db.session.commit()
        return "user kpi link created"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error

@api_bp.route('/api/user_kpis/<id>', methods=['DELETE'])
def delete_user_kpi(id):
    try:
        db.session.query(UserKpi).filter_by(id=id).delete()
        db.session.commit()
        return "user kpi link deleted"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/kpi_data', methods=['GET'])
def get_all_kpi_data():
    try:
        kpi_data = []
        for kpi in db.session.query(KpiData).all():
            del kpi.__dict__['_sa_instance_state']
            kpi_data.append(kpi.__dict__)
        return jsonify(kpi_data)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


@api_bp.route('/api/kpi_data/<id>', methods=['GET'])
def get_kpi_data(id):
    try:
        kpi_data = KpiData.query.get(id)
        del kpi_data.__dict__['_sa_instance_state']
        return jsonify(kpi_data.__dict__)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error