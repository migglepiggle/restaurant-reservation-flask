from app import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)  # NEW FIELD
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
