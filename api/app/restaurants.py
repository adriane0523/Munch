import os
from app import app, db
from app.models import User, Restaurant
from flask import render_template

@app.route('/get_restaurants/<query>')
def get_restaurants(query):
    pass

@app.route('/get_reccomended_restaurants/')
def get_reccomended_restaurants(query):
    pass


