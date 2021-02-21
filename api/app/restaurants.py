import os
from app import app, db
from app.models import User, Restaurant
from flask import render_template
import difflib
from flask import request, jsonify
import random

@app.route('/search')
def search():
    query = request.args.get('query', default="", type=str)
    print(query)
    result_query = []
    result=[]
    restaurants = Restaurant.query.all()
    for r in restaurants:
        types = r.munch_type.split(' | ')
        types.remove('')
        for t in types:
            seq = difflib.SequenceMatcher(None,query,t)
            seq_2 = difflib.SequenceMatcher(None,query, r.name)
            # or seq_2.ratio() > .7 
            if (seq.ratio() > .7):
                result.append(r)
                
        for i in result:
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


@app.route('/home')
def home():
    pass