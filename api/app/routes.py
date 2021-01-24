from app import app, db
from app.models import User
from flask_login import current_user, login_user, logout_user

from flask import request, jsonify
from werkzeug.urls import url_parse


@app.route('/check', methods=['GET'])
def check():
    if current_user.is_authenticated:
        return jsonify({'result': 'true'})

    return jsonify({'result': 'false'})


@app.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({'result': 'true'})

    json_data = request.json
    user_email = User.query.filter_by(email=json_data['username']).first()
    user_username = User.query.filter_by(username=json_data['username']).first()
    status = 'false'

    if user_email is not None:
        if (user_email.check_password(json_data['password'])):
            status = 'true'
            login_user(user_username,  remember=True)
        else:
            status = 'false'

    elif(user_username is not None):
        if (user_username.check_password(json_data['password'])):
            status = 'true'
            login_user(user_username,  remember=True)
        else:
            status = 'false'
    else:
        status = 'false'

    return jsonify({'result': status})

@app.route('/logout')
def logout():
    logout_user()
    return jsonify({'result': "Successfully Logout"})

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