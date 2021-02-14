from app import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import jwt
import datetime

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#user model
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)
    username = db.Column(db.String, unique=True, nullable=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String, unique=True, nullable=True)
    preferances = db.Column(db.String, nullable=True)
    firbase_id = db.Column(db.String, unique=True, nullable=True)
    registered_on = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=120),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }

            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e  

@staticmethod
def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

#friends model
class User_User(db.Model):
    __tablename__ = 'user_user'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_one_id = db.Column(db.Integer)
    user_two_id = db.Column(db.Integer)

#restaurant history
class User_Restaurant(db.Model):
    __tablename__ = 'user_restaurant'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    restaurant_munch_id = db.Column(db.Integer, nullable=True)
    time_spent = db.Column(db.Float, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    like = db.Column(db.Boolean, nullable=True)

class User_Menu_Item(db.Model):
    __tablename__ = 'user_menu_item'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    restaurant_munch_id = db.Column(db.Integer, nullable=True)
    menu_item_id = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    like = db.Column(db.Boolean, nullable=True)

#restaurant model
class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    place_id = db.Column(db.String, unique=True, nullable=True)
    name = db.Column(db.String, nullable=True)
    addr = db.Column(db.String, nullable=True)
    latitude = db.Column(db.String, nullable=True)
    longitude = db.Column(db.String, nullable=True)
    hours = db.Column(db.String, nullable=True)
    google_rating = db.Column(db.String, nullable=True)
    google_total_user_rating = db.Column(db.String, nullable=True)
    munch_rating = db.Column(db.String, nullable=True)
    google_type = db.Column(db.String, nullable=True)
    munch_type = db.Column(db.String, nullable=True)
    price_level = db.Column(db.String, nullable=True)

class Menu_Item(db.Model):
    __tablename__ = 'menu item'
    id = db.Column(db.Integer, primary_key=True)
    header_name = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    contains = db.Column(db.String, nullable=True)
    price = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)
    restaurant_id = db.Column(db.Integer, nullable=True)


#list of tokens
class TokenList(db.Model):
    __tablename__ = 'token list'
    id = db.Column(db.Integer, primary_key=True)
    auth_token = db.Column(db.String, unique=True, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    expiration = db.Column(db.DateTime, nullable=True)

    def __init__(self, auth_token, user_id):
        self.auth_token = auth_token
        self.user_id = user_id
        self.expiration = (datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=0))

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

