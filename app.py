import os

from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests

load_dotenv()
app = Flask(__name__)
GIPHY_API_KEY = os.getenv("API_KEY")
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    query = request.args.get('query', '')
    gifs = []

    if query:
        response = requests.get(
            f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={query}&limit=20'
        )
        if response.status_code == 200:
            data = response.json()
            gifs = [{
                'url': gif['images']['original']['url'],
                'title': gif['title']
            } for gif in data['data']]

    return render_template('index.html', gifs=gifs, query=query)

if __name__ == '__main__':
    app.run(debug=True)
