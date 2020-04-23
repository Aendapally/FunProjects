import json
from flask_cors import CORS
from flask import Flask
from main import Flames
app = Flask(__name__)
CORS(app)


@app.route('/<name1>/<name2>',methods=["POST","GET"])
def hello(name1,name2):
    flames = Flames()
    final_char = flames.check_chars(name1,name2)
    return json.dumps({"char": final_char})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
