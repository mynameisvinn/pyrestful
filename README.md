# microservices
a heavily annotated example of microservices, in order to explore what makes a "good" api. inspired by [cinema 3](https://github.com/umermansoor/microservices)

## pointing to an url is the same thing as calling a function
lets look at [movies](https://github.com/mynameisvinn/pyrestful/blob/master/services/movies.py) api. 

if visiting an url is similar to calling a function, then we can interpret flask's primary job as binding urls to functions (through the use of @app.route decorators):
```python
@app.route("/movies", methods=['GET'])
def movie_record():
    return nice_json(movies)
```
if urls are functions, then we should be able to pass arguments too! 
```python
@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    ...
    return nice_json(result)
```
the `url` contains a variable string called `<movieid>`. flask will take that variable and pass it to the function `movie_info()` as an argument.


finally, if pointing to an url is the equivalent of calling a function, we'd expect a return value. in many cases, the object returned is a json object, which can be rendered or manipulated by front end code.
```python
# @app.route("/movies", methods=['GET'])
# def movie_record():
    return nice_json(movies)
```