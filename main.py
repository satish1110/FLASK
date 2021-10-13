from flask import Flask, render_template , request  
from flasgger import Swagger 
import os


#WSGI 
app = Flask(__name__)
Swagger(app)

# mention request method, default GET 
@app.route('/', methods = ['GET'])  

# asynchronously 

def welcome():
    return "Learning swagger"

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome {your_name}"

@app.route('/check_request', methods = ['POST', 'GET'])
def get_req_parameters():

    """Practicing swagger
    ---
    parameters:
        - name: Student_name
          in: query
          type: string
          required: true
        - name: roll_no
          in: query
          type: number
          required: true
    responses:
        200:
            description: result is 
     """
    name = request.args.get("Student_name")
    roll = request.args.get("roll_no")

    # MESSAGE AND RESPONSE 
    return f"{name} {roll} studies in praxis", 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port = port, host = "0.0.0.0")
    
# fav icon 4040 since it's empty 

