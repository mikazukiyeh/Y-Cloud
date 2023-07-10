from flask import Flask

app = Flask(_name_)

@app.route("/",methods = ["GET"])
def home():
    return "OK"

if _name_ == "_main_":
    app.debug = Flase
    app.run(host = "0.0.0.0", port = 5001)

