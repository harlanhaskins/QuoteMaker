from flask import Flask, jsonify, request
import cardkov

app = Flask(__name__)

base = "/api"

max_quotes = 100

@app.route(base + "/quotes", methods=["GET"])
def quote():
    count = int(request.args.get("count", 1))
    count = max(1, min(count, 100))
    quotes = []
    for i in range(count):
        quotes.append(cardkov.new_string())
    return jsonify(quotes=quotes)

app.run(host="0.0.0.0", port=5585, debug=True)
