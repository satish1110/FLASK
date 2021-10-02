from flask import Flask, render_template  

#WSGI 
app = Flask(__name__)

# mention request method, default GET 
@app.route('/', methods = ['GET'])  

# asynchronously 

def welcome():
    return "Welcome to flask!"

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome {your_name}"


if __name__ == "__main__":
    app.run(debug=True, port = "8091")
    
# fav icon 4040 since it's empty 