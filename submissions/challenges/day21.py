from flask import Flask, Blueprint
app = Flask(__name__)

main_blueprint = Blueprint('main', __name__)

@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"

@main_blueprint.route('/')
def home():
    return "Welcome to the home page"

@main_blueprint.route('/about')
def about():
    return "This is the about page"

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()