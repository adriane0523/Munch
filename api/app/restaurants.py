import os
from app import app, db
from app.models import User, Restaurant, Menu_Item, User_Restaurant, TokenList, User_User
from flask import render_template
import difflib
from flask import request, jsonify
import random
import datetime

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def getKey(item):
    return item[1]

@app.route('/search',  methods=['GET', 'POST'])
def search():
    query = request.args.get('query', default="", type=str)
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()

    result_query = []
    result=[]
    restaurants = Restaurant.query.all()

    temp_liked_restaurants = User_Restaurant.query.filter_by(user_id=user.id)
    liked_restaurants = []

    for x in temp_liked_restaurants:
        i = Restaurant.query.filter_by(id=x.id).first()
        liked_restaurants.append(i)

    
    total_liked = ""
    for i in liked_restaurants:
        menu = ""
        for m in get_menu(i.id):
            menu_name = m["name"] + " "
            des = m["description"] + " "
            menu += ( menu_name + des )
        types = i.munch_type.replace('|', '')
        google_types = i.google_type.replace('|','')
        total_liked = types  + google_types + types + menu
    
    for r in restaurants:
        menu = ""
        for m in get_menu(r.id):
            menu_name = m["name"] + " "
            des = m["description"] + " "
            menu += ( menu_name + des )
        types = r.munch_type.replace('|', '')
        name = r.name + " "
        google_types = r.google_type.replace('|','')
        total = types + name + google_types + types + menu

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform([total])
        query_vec = vectorizer.transform([total_liked])
        results1 = cosine_similarity(X,query_vec)

        liked_vec = vectorizer.transform([query])
        results2 = cosine_similarity(X,liked_vec)
        results = (results1[0][0] * 0.3) + (results2[0][0] * 0.7)
        result.append([r, results])

    sorted_result = sorted(result, key=getKey)
    N = 10
    for index in sorted_result[-N:] :
        i = index[0]
        result_query.append( {
            "id":i.id,
            "place_id": i.place_id,
            "name": i.name,
            "addr": i.addr,
            "latitude": i.latitude,
            "longitude": i.longitude,
            "hours" : i.hours,
            "google_rating" : i.google_rating,
            "google_total_user_rating" : i.google_total_user_rating,
            "munch_rating" : i.munch_rating,
            "munch_type" : i.munch_type,
            "price_level" : i.price_level,
            "menu":get_menu(i.id),
            "percentage": index[1]
        })

    return {
        "result":result_query,
        "description":"query results"
    }

@app.route('/get_reccomended_restaurants/', methods=['GET', 'POST'])
def get_reccomended_restaurants(query):
    pass

def get_menu(id):
    m = Menu_Item.query.filter_by(restaurant_id=id).all()
    result = []
    for i in m:
        result.append(
            {
                "header_name":i.header_name,
                "name":i.name,
                "description":i.description,
                "contains":i.contains,
                "price":i.price,
                "image":i.image,
                "restaurant_id":i.restaurant_id
            }
        )
    
    return result

@app.route('/get_restaurant', methods=['GET', 'POST'])
def get_restaurant():
    query = request.args.get('query', default="", type=int)
    restaurants = Restaurant.query.filter_by(id=query).first()
    i = restaurants
    result= {
            "id":i.id,
            "place_id": i.place_id,
            "name": i.name,
            "addr": i.addr,
            "latitude": i.latitude,
            "longitude": i.longitude,
            "hours" : i.hours,
            "google_rating" : i.google_rating,
            "google_total_user_rating" : i.google_total_user_rating,
            "munch_rating" : i.munch_rating,
            "google_type" : i.google_type,
            "munch_type" : i.munch_type,
            "price_level" : i.price_level,
            "menu":get_menu(i.id)
    }
    print(result)
    return  jsonify(result)

@app.route('/home', methods=['GET', 'POST'])
def home():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()

    temp_liked_restaurants = User_Restaurant.query.filter_by(user_id=user.id)
    liked_restaurants = []
    user_user1 = User_User.query.filter_by(user_one_id=user.id)
    user_user2 = User_User.query.filter_by(user_two_id=user.id)
    restaurants = Restaurant.query.all()

    for x in temp_liked_restaurants:
        i = Restaurant.query.filter_by(id=x.id).first()
        liked_restaurants.append(i)
    

    friend_liked_restaurant = []
    friend = []
    result_restaurants = []
    
    for i in user_user1:
        user_friend = User.query.filter_by(id=i.user_two_id).first()
        liked_restaurants_friend = User_Restaurant.query.filter_by(user_id=user_friend.id)
        friend.append({"username":user_friend.username})
        for i in liked_restaurants_friend:
            friend_liked_restaurant.append(i)

    for i in user_user2:
        user_friend = User.query.filter_by(id=i.user_one_id).first()
        if (user_friend.username not in friend):
            liked_restaurants_friend = User_Restaurant.query.filter_by(user_id=user_friend.id)
            friend.append({"username":user_friend.username})
            for i in liked_restaurants_friend:
                if friend_liked_restaurant not in friend_liked_restaurant:
                    friend_liked_restaurant.append(i)


    total_liked = ""
    for i in liked_restaurants:
        menu = ""
        for m in get_menu(i.id):
            menu_name = m["name"] + " "
            des = m["description"] + " "
            menu += ( menu_name + des )
        types = i.munch_type.replace('|', '')
        google_types = i.google_type.replace('|','')
        total_liked = types  + google_types + types + menu

    for r in restaurants:
        menu = ""
        total_restaurants = ""    
        for m in get_menu(r.id):
            menu_name = m["name"] + " "
            des = m["description"] + " "
            menu += ( menu_name + des )
        types = r.munch_type.replace('|', '')
       
        google_types = r.google_type.replace('|','')
        total_restaurants = types  + google_types + types + menu

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform([total_restaurants])
        query_vec = vectorizer.transform([total_liked])
        results = cosine_similarity(X,query_vec)

        if (r not in liked_restaurants):
            result_restaurants.append([r, results[0][0]])

    for i in result_restaurants:
        flag = True
        for x in friend_liked_restaurant:
            if x == i:
                flag = False
                i[1] = (float)((i[1] * .4) + (1 * .6))
        if (flag):
            i[1] = (float)((i[1] * .4) + (0 * .6))

    result = []
    sorted_result = sorted(result_restaurants, key=getKey)
    N = 10
    for index in sorted_result[-N:] :
        i = index[0]
        result.append( {
            "id":i.id,
            "place_id": i.place_id,
            "name": i.name,
            "addr": i.addr,
            "latitude": i.latitude,
            "longitude": i.longitude,
            "hours" : i.hours,
            "google_rating" : i.google_rating,
            "google_total_user_rating" : i.google_total_user_rating,
            "munch_rating" : i.munch_rating,
            "munch_type" : i.munch_type,
            "price_level" : i.price_level,
            "menu":get_menu(i.id),
            "percentage": index[1]
        })

    return  jsonify({'result': result,
                    'description': "fetched home restaurant items"
                    })


@app.route('/random', methods=['GET', 'POST'])
def get_random():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    liked_restaurants = User_Restaurant.query.filter_by(user_id=user.id)
    restaurants = Restaurant.query.all()
    count = 0
    result = []
    restaurants = random.shuffle(restaurants)
    while (count <= 5):
        i = restaurants[count]
        result.append( {
                "id":i.id,
                "place_id": i.place_id,
                "name": i.name,
                "addr": i.addr,
                "latitude": i.latitude,
                "longitude": i.longitude,
                "hours" : i.hours,
                "google_rating" : i.google_rating,
                "google_total_user_rating" : i.google_total_user_rating,
                "munch_rating" : i.munch_rating,
                "munch_type" : i.munch_type,
                "price_level" : i.price_level,
                "menu":get_menu(i.id)
        })
        flag = True
        for x in liked_restaurants:
            if (i.id == x.restaurant_munch_id):
                flag = False
        if (flag):
            count+=1
            
    return  jsonify({'result': result,
                    'description': "fetched 5 random restaurant items"
                    })

   
@app.route('/like_restaurant', methods=['GET', 'POST'])
def like_restaurant():
    json_data = request.json
    query = request.args.get('query', default="", type=int)
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    liked_restaurants = User_Restaurant.query.filter_by(user_id=user.id)
    flag = True
    for i in liked_restaurants:
        if i.restaurant_munch_id == query:
            flag = False
    x = None
    if (flag):
        x = User_Restaurant(
            user_id = user.id,
            restaurant_munch_id = query,
            time_spent = 0,
            rating = 0,
            like = True,
            timestamp = datetime.datetime.utcnow(),
        )
        status = ''
        try:
            db.session.add(x)
            db.session.commit()
            status = 'True'
        except:
            status = 'False'
        db.session.close()
    else:
        status = 'False'

    return  jsonify({'result': status,
                'description': "Liked restaurant with an id of " + format(query)
                })


@app.route('/get_like_restaurant',  methods=['GET', 'POST'])
def get_like_restaurant():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    liked_restaurants = User_Restaurant.query.filter_by(user_id=user.id)

    result = []
    for x in liked_restaurants:
        i = Restaurant.query.filter_by(id=x.id).first()
        result.append( {
                "id":i.id,
                "place_id": i.place_id,
                "name": i.name,
                "addr": i.addr,
                "latitude": i.latitude,
                "longitude": i.longitude,
                "hours" : i.hours,
                "google_rating" : i.google_rating,
                "google_total_user_rating" : i.google_total_user_rating,
                "munch_rating" : i.munch_rating,
                "munch_type" : i.munch_type,
                "price_level" : i.price_level,
                "menu":get_menu(i.id)
        })
        
    return  jsonify(result)

