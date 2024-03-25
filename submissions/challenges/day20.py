
from flask import Flask 

  
app = Flask(__name__) 
  
# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"
    
@app.route("/") 
def index(): 
    return "Homepage of GeeksForGeeks"

@app.route("/panget")
def hihi():
    return "oo na panget ka na"

@app.route("/user/<username>")
def user_prof(username):
    return f'welcome, {username}!'
  
if __name__ == "__main__": 
    app.run(debug=True) 

def decor(func):
    def wrapper(*args, **kwargs):
        print("Something is happening in the function!")
        func(*args, **kwargs)
        print("Ended")
    return wrapper

@decor
def add(x, y):
    sum = x + y
    print (f"{x} + {y} = {sum}")

add(3, 5)


    