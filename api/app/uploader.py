import os
from app import app, db
from app.models import User, Restaurant, Menu_Item
from flask import render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileAllowed, FileRequired, FileField
from werkzeug.utils import secure_filename


file_path = './photos/'
images = UploadSet('images', IMAGES)
class MenuForm(FlaskForm):
    name = StringField('Name', validators=[])
    header_name = StringField('Header name', validators=[])
    description = StringField('Description', validators=[])
    contains = StringField('Contains', validators=[])
    price = StringField('Price', validators=[])
    image = FileField('Image', validators=[])
    submit = SubmitField('Submit')

 

@app.route('/edit_menu/<id>', methods=['GET', 'POST'])
def edit_menu(id):
    r = Restaurant.query.filter_by(id=id).first()
    m = Menu_Item.query.filter_by(restaurant_id=id)
    form = MenuForm()
    print(form.name.data)
    print(form.header_name.data)
    print(form.description.data)
    print(form.price.data)
    print(form.image.data)
    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(file_path, filename))
     
        return "Sucessfully uploaded"
    else:
        print("failed")
    return render_template('index.html', title=r.name, menu_item=m,id=id, form=form)


@app.route('/')
def restaurants():
    r = Restaurant.query.all()
    return render_template('restaurant.html', restaurants=r)
    


@app.route('/get/<id>')
def get(id):
    r = Restaurant.query.filter_by(id=id).first()

    return jsonify({
        "id":r.id,
        "place_id": r.place_id,
        "name": r.name,
        "addr": r.addr,
        "latitude": r.latitude,
        "longitude": r.longitude,
        "hours" : r.hours,
        "google_rating" : r.google_rating,
        "google_total_user_rating" : r.google_total_user_rating,
        "munch_rating" : r.munch_rating,
        "munch_type" : r.munch_type,
        "price_level" : r.price_level,
    })
    

@app.route('/edit/<id>')
def edit(id):
    json_data = request.json
    r = Restaurant.query.filter_by(id=id).first()
    r.name = json_data["name"]
    r.addr = json_data["addr"]
    r.latitude = json_data["latitude"]
    r.longitude = json_data["longitude"]
    r.hours = json_data["hours"]
    r.google_rating = json_data["google_rating"]
    r.google_total_user_rating = json_data["google_total_user_rating"]
    r.munch_rating = json_data["munch_rating"]
    r.munch_type = json_data["munch_type"]
    r.price_level = json_data["price_level"]

    db.session.commit()
    
    return jsonify({'result': "success",
                    'description': "Successfully added items to restaurants"})

@app.route('/add_menu/<id>')
def add_menu(id):
    json_data = request.json    
    r = Restaurant.query.filter_by(id=id).first()
    print(json_data)
    if (r == None):
        return jsonify({'result': "failed",
                    'description': "failed to add menu items"})
 
    menu = Menu_Item(
        header_name = json_data["header_name"],
        name = json_data["name"],
        description = json_data["description"],
        contains = json_data["contains"],
        price = json_data["price"],
        image = json_data["image"],
        restaurant_id = r.id
    )
    
    return jsonify({'result': "sucess",
                    'description': "successfully to add menu items"})



@app.route('/get_menu/<id>')
def get_menu(id):
    m = Menu_Item.query.filter_by(id=id)
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
    
    return jsonify({'result': result,
                    'description': "fetched menu items"})