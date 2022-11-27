from flask import Blueprint, render_template
from flask_login import login_required, current_user
from src.models.user_kpi import UserKpi
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
    for kpi in db.session.query(UserKpi).all():
        del kpi.__dict__['_sa_instance_state']
        kpis.append(kpi.__dict__)
    return render_template('profile.html', name=current_user.name, kpis=kpis)
