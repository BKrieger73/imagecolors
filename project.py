from flask import Flask
import datetime as dt
import time as t

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>" + str(int(t.time())) + "</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
