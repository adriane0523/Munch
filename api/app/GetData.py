from googleplaces import GooglePlaces, types, lang
import json
from decimal import Decimal

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

from app import app, db
from app.models import Restaurant, Menu 

from flask import request, jsonify
from werkzeug.urls import url_parse
import jwt
import datetime


def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)


COORDINATES_1 = [(33.4255, -111.9400), (33.421950, -111.952157), (33.421950, -111.926450), (33.451353, -111.926622), (33.429058, -111.908908),
                (33.42010,-111.909197), (-33.42010, -111.926375), (33.422040, -111.951997), (33.422101, -111.934783), (33.421789, -111.960830), #tempe
               # (33.3062, -111.8413), #chandler
               # (33.4484, -112.0740), #phx
               # (33.4942, -111.9261), #scottsdale
               # (33.3528, -111.7890), #glibert
               # (33.5806, -112.2374), #peoria
               # (33.5387, -112.1860), #glendale
               # (33.4152, -111.8315), #mesa
                ]

COORDINATES = [(33.4255, -111.9400)]
RESTAURANT_TYPE = ["vegan", "vegetarian", "american", "chinese", "cajun", "arabic", "Indian", "filipino", "jamaican",
"hamburger", "italian", "greek", "southern", "chicken", "steak", "mediterranean", "turkish", "dim sum" "british", "English", "african", "sushi",
"seafood", "east-european", "polish", "thai", "vietnamese", "hwaiian", "mexcian", "chicken wings", "pizza", "japanese", "asian", "korean",  "barbecue"]

@app.route('/google_places', methods=['GET'])
def google_places():
    YOUR_API_KEY = 'AIzaSyBZmVjjr2QxBHa6UzRC9lEX-JjrqbmXGeY'
    google_places = GooglePlaces(YOUR_API_KEY)
    # You may prefer to use the text_search API, instead.

    v = []
    restaurants_id = []
    count = 0
    for x in RESTAURANT_TYPE:
        flag = False
        for i in COORDINATES:
            print(x)
            query_result = google_places.nearby_search(lat_lng={'lat':i[0], 'lng':i[1]}, location="Arizona", keyword=x,  types=[types.TYPE_RESTAURANT], radius=5000)

            for v in Restaurant.query.all():
                if v.place_id not in restaurants_id:
           
                    restaurants_id.append(v.place_id)

            for place in query_result.places:
                if place.place_id not in restaurants_id :
                    print (place.name, " : ", place.place_id)
                    restaurants_id.append(place.place_id)
                    place.get_details()
                
                    hours_temp = ""
                    try:
                        for i in place.details["opening_hours"]["weekday_text"]:
                            hours_temp+= i + " | "
                    except:
                        hours_temp = ""
            
                    time_temp = ""
                    try:
                        for i in place.details["types"]:
                            time_temp += i + " | "
                    except:
                        time_temp = ""
                
                    price = ""
                    try:
                        price = place.details["price_level"]
                    except:
                        price = ""

                    name = place.name
                    place_id = place.place_id
                    addr = (str)(place.details["formatted_address"])
                    lat = (str)(place.details["geometry"]["location"]["lat"])
                    lng = (str)(place.details["geometry"]["location"]["lng"])
                    hours = hours_temp

                    google_rating = ""
                    try:  
                        google_rating = (str)(place.details["rating"])
                    except:
                        google_rating = ""

                    google_total_user_rating = ""
                    try:
                        google_total_user_rating = (str)(place.details["user_ratings_total"])
                    except:
                        google_total_user_rating = ""

                    munch_rating = ""
                    google_type = time_temp
                    munch_type = x + " | "
                    price_level = price
                    menu = Menu()
                    restaurnat = Restaurant(name=name, place_id=place_id,addr=addr, latitude=lat,longitude=lng, hours=hours, google_rating=google_rating, google_total_user_rating=google_total_user_rating,
                                            munch_rating=munch_rating, google_type=google_type, munch_type=munch_type,price_level=price_level)
                    db.session.add(restaurnat)
                    db.session.commit()
       
        
                
                elif place.place_id in restaurants_id:
                    r = Restaurant.query.filter_by(place_id=place.place_id).first()
                    if x not in r.munch_type:
    
                        temp = r.munch_type
                        temp =  temp + x + " | " 
                        #r.munch_type = temp
                        print("Addeed",x, "to", place.place_id )
                        print()
                        time.sleep(1)
                        r.munch_type = temp
                        db.session.commit()
                    
                
       
        
    return "Success"
   
                #time.sleep(1)
             