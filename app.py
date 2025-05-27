from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GIPHY_API_KEY = 'IX3uGkEBhdddaCBmUkyF6vgS4PdJ35cz'

@app.route('/', methods=['GET', 'POST'])
def index():
    gifs = []
    if request.method == 'POST':
        termo = request.form['termo']
        url = f'https://api.giphy.com/v1/gifs/search'
        params = {
            'api_key': GIPHY_API_KEY,
            'q': termo,
            'limit': 5
        }
        response = requests.get(url, params=params)
        data = response.json()
        gifs = [item['images']['original']['url'] for item in data['data']]
    return render_template('index.html', gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
