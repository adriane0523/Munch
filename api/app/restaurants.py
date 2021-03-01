import os
from app import app
from app.models import User, Restaurant, Menu_Item, User_Restaurant
from flask import render_template
import difflib
from flask import request, jsonify
import random

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def getKey(item):
    return item[1]

@app.route('/search')
def search():
    query = request.args.get('query', default="", type=str)

    result_query = []
    result=[]
    restaurants = Restaurant.query.all()
    #restaurants = Restaurant.query.filter_by(id=1).all()
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
        query_vec = vectorizer.transform([query])
        results = cosine_similarity(X,query_vec)
        result.append([r, results[0][0]])

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
        })

    return {
        "result":result_query,
        "description":"query results"
    }

@app.route('/get_reccomended_restaurants/')
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

@app.route('/get_restaurant', methods=['GET'])
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

@app.route('/home', methods=['POST'])
def home():
    restaurants = Restaurant.query.all()
    count = 0
    result = []
    while (count <= 10):
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

        count+=1
    return  jsonify({'result': result,
                    'description': "fetched restaurant items"
                    })


@app.route('/random', methods=['POST'])
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

   
@app.route('/like_restaurant', methods=['GET'])
def like_restaurant():
    query = request.args.get('query', default="", type=int)
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    liked_restaurant = User_Restaurant(
        user_id = user.id,
        restaurant_munch_id = query,
        time_spent = 0,
        rating = 0,
        like = True,
    )
    status = ''
    try:
        db.session.add(liked_restaurant)
        db.session.commit()
        status = 'True'
    except:
        status = 'False'
    db.session.close()

    return  jsonify({'result': status,
                'description': "Liked restaurant with an id of " + json_data['restaurant_id']
                })


@app.route('/get_like_restaurant', methods=['POST'])
def get_like_restaurant():
    json_data = request.json
    tokenList = TokenList.query.filter_by(auth_token=json_data['auth_token']).first()
    user = User.query.filter_by(id=tokenList.user_id).first()
    liked_restaurants = User_Restaurant.query.filter_by(user_id=user.id)

    result = []
    for x in likeliked_resaurants:
        i = Restaurant.filter_by(id=x.id).first()
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
        
    return  jsonify({'result': result,
                    'description': "fetched liked restaurant items"
                    })

