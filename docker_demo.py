from flask import Flask  

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def welcome():
    return f"Welcome to docker!"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
