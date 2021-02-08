import os
from app import app, db
from app.models import User, Restaurant
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get/<id>')
def get(id):
    restaurant = Restaurant.query.filter_by(id=id).first()
    print(restaurant)
    

@app.route('/upload/<id>')
def upload(id):
    pass

