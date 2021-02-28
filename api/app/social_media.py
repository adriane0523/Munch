from app import app
from app.models import User, User_User

@app.route('/friend', methods=['POST'])
def friend():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    user_friend = User.query.filter_by(username=json_data['username']).first()
    result = ''
    if (user_friend != None):
        user_user = User_User(  user_one_id = user.id, user_two_id = user_friend)
        result = 'true'
    else
        user_user = None
        result = 'false'

    return jsonify({'result': result,
        'description': 'Friending a user'})

@app.route('/get_friends', methods=['POST'])
def get_friends():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    user_user = User_User.query.filter_by(user_one_id=user.id)

    result = []
    for i in user_user:
        user_friend = User.query.filter_by(username=i.user_two_id).first()
        result.append(user_friend.username)


    return jsonify({'result': result,
        'description': 'Fetched Friends List'})

