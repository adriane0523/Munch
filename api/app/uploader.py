import os
from app import app, db
from app.models import User, TokenList
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
