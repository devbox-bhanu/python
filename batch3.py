from datetime import datetime

from flask import flask

app = Flask(_name_)

@app.route("/")
def home():
    date = datetime.now()
    return str(date)

if _name_ == "_main_":
    app.run(host='0.0.0.0',port=5000)
