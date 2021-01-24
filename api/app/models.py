from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#user model
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)
    username = db.Column(db.String, unique=True, nullable=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String, unique=True, nullable=True)
    preferances = db.Column(db.String, nullable=True)
    firbase_id = db.Column(db.String, unique=True, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)    

#friends model
class User_User(db.Model):
    __tablename__ = 'user_user'
    id = db.Column(db.Integer, primary_key=True)
    user_one_id = db.Column(db.Integer, primary_key=True)
    user_two_id = db.Column(db.Integer, primary_key=True)

#restaurant history
class User_Restaurant(db.Model):
    __tablename__ = 'user_restaurant'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    restaurant_munch_id = db.Column(db.Integer, nullable=True)
    time_spent = db.Column(db.Float, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    like = db.Column(db.Boolean, nullable=True)

#restaurant model
class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.String, unique=True, nullable=True)
    food_images = db.Column(db.String, unique=True, nullable=True)
