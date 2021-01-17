from app import app

@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"