from flask import Blueprint, render_template
from flask_login import login_required, current_user
from src.models.user_kpi import UserKpi
from src.models.user import User
from src.models.kpi import Kpi
from src import db

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='/assets')


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/profile')
@login_required
def profile():
    kpis = []
    for kpi in db.session.query(Kpi).join(UserKpi).join(User).filter(
        User.email == current_user.email
        ).all():
        del kpi.__dict__['_sa_instance_state']
        kpis.append(kpi.__dict__)
    if not kpis:
        return render_template('profile.html', name=current_user.name, 
        submission_status='You have no assigned kpis to submit')
    else:
        return render_template('profile.html', name=current_user.name, 
        submission_status='You can submit data for:', kpis=[f"{i.get('name')} ({i.get('description')})" for i in kpis])


@main_bp.route('/submit')
@login_required
def submit():
    kpis = []
    for kpi in db.session.query(Kpi).join(UserKpi).join(User).filter(
        User.email == current_user.email
        ).all():
        del kpi.__dict__['_sa_instance_state']
        kpis.append(kpi.__dict__)
    if not kpis:
        return render_template('submit.html', name=current_user.name, 
        submission_status='You have no assigned kpis to submit')
    else:
        return render_template('submit.html', name=current_user.name, 
        submission_status='Choose the KPI to submit', kpis={i.get('name'): i.get('description') for i in kpis})