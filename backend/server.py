from flask import Flask, jsonify, request, Response, json, make_response
from flask_cors import CORS
import argparse
from homestarkov import Homestarkov
from hitcounter import HitCounter

app = Flask(__name__)
cors = CORS(app)

base = "/api"

_characters = {
    "cardgage": Homestarkov("cardgage", "Senor Cardgage",
        "Dump Tell No Mandy!"),
    "homsar": Homestarkov("homsar", "Homsar", "Legitimate Business!")
}

hits_counter = HitCounter()

max_quotes = 100

@app.before_request
def log_hit():
    hits_counter.add_hit()

@app.route(base + "/characters", methods=["GET"])
def characters():
    character_list = [c.json_object() for c in _characters.values()]
    return jsonify(characters=character_list)

@app.route(base + "/quotes/<character>", methods=["GET"])
def quote(character):
    if not character in _characters:
        return make_response("Invalid character: %s" % character, 401)

    markov = _characters[character]

    count_string = request.args.get("count", "1")
    count = int(count_string) if count_string.isdigit() else 1
    count = max(1, min(count, 100))
    quotes = []
    for i in range(count):
        quotes.append(markov.new_string())

    return jsonify(quotes=quotes)

@app.teardown_request
def print_count(*args):
    print(len(hits_counter))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="Runs flask in debug mode.",
                          action="store_true")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=5586 if args.test else 5585, debug=args.test)
