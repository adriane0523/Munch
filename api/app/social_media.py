from app import app, db
from app.models import User, User_User, TokenList
from flask import request, jsonify
import datetime

@app.route('/friend', methods=['POST'])
def friend():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    user_friend = User.query.filter_by(username=json_data['username']).first()

    result = ''
    if (user_friend != None):
        checkUser1 = User_User.query.filter_by(user_one_id=user_friend.id).first()
        checkUser2 = User_User.query.filter_by(user_two_id=user_friend.id).first()
        if (checkUser1 == None and checkUser2 == None ):
            user_user = User_User(  user_one_id = user.id, user_two_id = user_friend.id, timestamp = datetime.datetime.utcnow())
            try:
                db.session.add(user_user)
                db.session.commit()
                result = 'True'
            except:
                result = 'False'
            db.session.close()
        else:
            user_user = None
            result = 'False'
    else:
        user_user = None
        result = 'False'
    return jsonify({'result': result,
        'description': 'Friending a user'})

@app.route('/get_friends', methods=['POST'])
def get_friends():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    user_user1 = User_User.query.filter_by(user_one_id=user.id)
    user_user2 = User_User.query.filter_by(user_two_id=user.id)

    result = []
    for i in user_user1:
        user_friend = User.query.filter_by(id=i.user_two_id).first()
          
        result.append({"username":user_friend.username})

    for i in user_user2:
        user_friend = User.query.filter_by(id=i.user_one_id).first()
        if (user_friend.username not in result):
            result.append({"username":user_friend.username})
    
    print(result)
    return jsonify({'result': result,
        'description': 'Fetched Friends List'})

