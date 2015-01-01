from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import argparse
from homestarkov import Homestarkov

app = Flask(__name__)
cors = CORS(app)

base = "/api"

characters = {
    "cardgage": Homestarkov("cardgage"),
    "homsar": Homestarkov("homsar")
}

max_quotes = 100

@app.route(base + "/quotes/<character>", methods=["GET"])
def quote(character):
    if not character in characters:
        return make_response("Invalid character: %s" % character, 401)

    markov = characters[character]

    count_string = request.args.get("count", "1")
    count = int(count_string) if count_string.isdigit() else 1
    count = max(1, min(count, 100))
    quotes = []
    for i in range(count):
        quotes.append(markov.new_string())

    return jsonify(quotes=quotes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="Runs flask in debug mode.",
                          action="store_true")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=5585, debug=args.test)
