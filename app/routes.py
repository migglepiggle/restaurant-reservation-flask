from flask import Blueprint, render_template, request, redirect, flash
from app.models import Reservation
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    reservations = Reservation.query.all()
    return render_template('index.html', reservations=reservations)

@bp.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']

    new_reservation = Reservation(name=name, phone=phone, date=date, time=time)
    db.session.add(new_reservation)
    db.session.commit()
    flash('Reservation added!')
    return redirect('/')
