from utils import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("{}/database/showtimes.json".format(root_dir()), "r") as f:
    showtimes = json.load(f)


# no argument was passed, so this is a dummy placeholder
@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "showtimes": "/showtimes",
            "showtime": "/showtimes/<date>"
        }
    })

# if no date arugment is passed, then return all possible showtimes
@app.route("/showtimes", methods=['GET'])
def showtimes_list():
    return nice_json(showtimes)


# if a date argument is passed, then use it to fetch the approprate key/value pair
@app.route("/showtimes/<date>", methods=['GET'])
def showtimes_record(date):
    if date not in showtimes:
        raise NotFound
    print (showtimes[date])
    return nice_json(showtimes[date])

if __name__ == "__main__":
    app.run(port=5002, debug=True)  # each microservice is exposed through a unique port