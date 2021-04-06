from app import app, db
from app.models import User, TokenList
from flask_login import current_user, login_user, logout_user

from flask import request, jsonify
from werkzeug.urls import url_parse
import jwt
import datetime

@app.route('/logout', methods=['POST'])
def logout():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    db.session.delete(tokenList)
    db.session.commit()
    status = 'true'
    message = "Succesfully logged out"

    return jsonify({'result': status,
            'description': message})

@app.route('/check_login', methods=['POST'])
def check_login():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    username = ""
    
    if tokenList is not None:
        if (datetime.datetime.utcnow() < tokenList.expiration):
            status = 'true'
            message = "Successfully logged in."
            
            user = User.query.filter_by(id=tokenList.user_id).first()
            username = user.username
        else:
            tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
            db.session.delete(tokenList)
            db.session.commit()
            status = 'false'
            message = "Failed to log in - expired token"

    else:
        status = 'false'
        message = "Can not find token"

    return jsonify({'result': status,
                    'description': message,
                    'username': username})

    
def addTokenList(user_id, auth_token):
    tokenList = TokenList(user_id=user_id, auth_token=auth_token)
    db.session.add(tokenList)
    db.session.commit()
    print("Added token to database")


@app.route('/login', methods=['POST'])
def login():
    json_data = request.json
    user_email = User.query.filter_by(email=json_data['username']).first()
    user_username = User.query.filter_by(username=json_data['username']).first()
    status = 'false'
    auth_token = "None"
    message = "Failed to log in."

    if user_email is not None:
        if (user_email.check_password(json_data['password'])):
            status = 'true'
            login_user(user_email,  remember=True)
            auth_token = user_email.encode_auth_token(user_id=user_email.id)
            if auth_token:
                message = "Successfully logged in."
                auth_token = auth_token.decode()
                addTokenList(user_email.id, auth_token)
             
        else:
            status = 'false'

    elif(user_username is not None):
        if (user_username.check_password(json_data['password'])):
            status = 'true'
            login_user(user_username,  remember=True)
            auth_token = user_username.encode_auth_token(user_id=user_username.id)
            if auth_token:
                message = "Successfully logged in."
                auth_token = auth_token.decode()
                addTokenList(user_username.id, auth_token)
                
        else:
            status = 'false'
    else:
        status = 'false'

    return jsonify({'result': status,
                    'description': message,
                    'auth_token': auth_token})


@app.route('/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        return jsonify({
            'result': 'True',
            'email': 'True',
            'username':'True'
                        })
    json_data = request.json
    print(json_data)

    user_username = User.query.filter_by(username=json_data['username']).first()

    if user_username is not None:
        return jsonify({
            'result': 'User already registered',
                        })

    valid_email = validate_email(json_data['email'])
    valid_username = validate_username(json_data['username'])
    status = 'False'
    if (valid_email and valid_username):
        user = User(
            email=json_data['email'],
            username=json_data['username']
        )
        user.set_password(json_data['password'])

        try:
            db.session.add(user)
            db.session.commit()
            status = 'True'
        except:
            status = 'False'
        db.session.close()

    return jsonify({'result': status,
                    'email': valid_email,
                    'username': valid_username})

def validate_username(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return False
    return True

def validate_email(email):
    user = User.query.filter_by(email=email).first()
    if user is not None:
        return False
    return True

@app.route('/get_username', methods=['POST'])
def get_username():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()

    status = 'True'
    message = "fetched username"

    return jsonify({'result': status,
            'username' : user.username,
            'description': message})
