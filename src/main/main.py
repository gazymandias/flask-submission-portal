from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from src.models.user_kpi import UserKpi
from src.models.user import User
from src.models.kpi import Kpi
from src.models.kpi_data import KpiData
from src import db
from sqlalchemy import func

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
        submission_status='Choose the KPI to submit', kpis={i.get('id'): i.get('name') for i in kpis})


@main_bp.route('/submit', methods=['POST'])
def submit_post():
    # code to validate submission goes here e.g. numerator bigger than denominator
    kpi_id = request.form.get('kpi_id')
    month = request.form.get('month')
    year = request.form.get('year')
    numerator = request.form.get('numerator')
    denominator = request.form.get('denominator')

    if numerator > denominator: # on error redirect back to submit page so user can try again
        flash(u'The numerator cannot be greater than the denominator', 'error')
        return redirect(url_for('main_bp.submit'))

    from datetime import datetime
    d = datetime.strptime(month+year, '%B%Y')
    new_kpi_data = KpiData(date=d, user_id=current_user.id, kpi_id=kpi_id, numerator=numerator, denominator=denominator, submitted_at=func.now())
    db.session.add(new_kpi_data)
    db.session.commit()
    flash(u'Thanks for submitting!', 'info')
    return redirect(url_for('main_bp.submit'))
