from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    query = request.args.get("name") #how to access input query
    params = {
        "q": query,
        "key": "7KOU0A3XQ2BG",
        "limit" : 10
    }
    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
    r = requests.get("https://api.tenor.com/v1/search", params)
    
    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    # gifs = json.loads(r.content)
    gifs = r.json()
    gif_results = gifs['results']
    print(gif_results)

    # gif_results = list()
    # for i in range(params['limit']):
    #     gif_results.append(gifs['results'][i]['url']) #gifs['results'][0]['id'], gifs['results'][0]['itemurl'])
        
    
    return render_template("index.html", gif_results=gif_results)


    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    

if __name__ == '__main__':
    app.run(debug=True)
