from flask import Flask, render_template , request  

#WSGI 
app = Flask(__name__)

# mention request method, default GET 
@app.route('/', methods = ['GET'])  

# asynchronously 

def welcome():
    return render_template("index.html")

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome {your_name}"

@app.route('/check_request')
def get_req_parameters():
    name = request.args.get("name")
    roll = request.args.get("roll")
    return f"{name} {roll} studies in praxis", 206 

if __name__ == "__main__":
    app.run(debug=True, port = "8091")
    
# fav icon 4040 since it's empty 