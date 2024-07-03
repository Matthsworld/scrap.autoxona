from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
'''
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')
'''
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    home_address = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(50), nullable=False)
    registration_number = db.Column(db.String(50), nullable=False)
    photos = db.Column(db.String(300), nullable=False)
    attended = db.Column(db.Boolean, default=False)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner_name = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    home_address = db.Column(db.String(150), nullable=False)
    vehicle_registration = db.Column(db.String(50), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(50), nullable=False)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    home_address = db.Column(db.String(150), nullable=False)
    vehicle_registration = db.Column(db.String(50), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(50), nullable=False)
    response = db.Column(db.String(500), nullable=True)  # To store admin's response
