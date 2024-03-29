from utils import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json

app = Flask(__name__)

# load data into memory; 
with open("{}/database/movies.json".format(root_dir()), "r") as f:
    movies = json.load(f)

# app.route binds url to function; a good example of an decorator
@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    })

# triggered by http://127.0.0.1:5001/movies/7daf7208-be4d-4944-a3ae-c1c2f516f3e6
@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    if movieid not in movies:
        raise NotFound
    result = movies[movieid]
    result["uri"] = "/movies/{}".format(movieid)
    return nice_json(result)

# triggered by http://127.0.0.1:5001/movies
@app.route("/movies", methods=['GET'])
def movie_record():
    return nice_json(movies)

if __name__ == "__main__":
    app.run(port=5001, debug=True)  # each microservice will have a unique port

