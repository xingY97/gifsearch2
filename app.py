from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get("q")
    params = {
        "q": query,
        "key": "7KOU0A3XQ2BG",
        "limit" : 9
    }

    r = requests.get("https://api.tenor.com/v1/search", params)
    gifs = r.json()
    gif_results = gifs['results']
    
    return render_template("index.html", gif_results=gif_results)

if __name__ == '__main__':
    app.run(debug=True)
