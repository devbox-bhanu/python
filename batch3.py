from datetime import datetime
from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    date = datetime.now()
    return str(date)

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=4000)
