from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function

    flicks = get_random_movie()
    

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + flicks[0] + "</li>"
    content += "</ul>"
    

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + flicks[1] + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ["The Big Lebowski", "Office Space", "Idiocracy", 
    "The Wall", "National Lampoon's: Christmas Vaction", 
    "The Karate Kid", "Ghostbusters", "Goldfinger", "The Goonies"]
    picks = random.sample(movies, 2)
    
    #return movies[pick]
    return picks

app.run()
