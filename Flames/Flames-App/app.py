import json
from flask_cors import CORS
from flask import Flask
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return json.dumps({"message":"Hello World from server 12345!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
