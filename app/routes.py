from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Reservation

main = Blueprint('main', __name__)

@main.route('/')
def index():
    reservations = Reservation.query.all()
    return render_template('index.html', reservations=reservations)

@main.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']

    new_reservation = Reservation(name=name, phone=phone, date=date, time=time)
    db.session.add(new_reservation)
    db.session.commit()
    return redirect(url_for('main.index'))
