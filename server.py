import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def compare():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    try:
        if a > b:
            return Response(json.dumps({"status":"a>b"}), mimetype="application/json")
        else:
            return Response(json.dumps({"status":"a<=b"}), mimetype="application/json")
    except:
        return Response(json.dumps({"status":"invalid parameter"}), status = 403, mimetype="application/json")

if __name__ == "__main__":
    app.debug = False
    app.run(host = "0.0.0.0", port = 5001)
