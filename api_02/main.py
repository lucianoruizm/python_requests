import requests
import os
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv('API_KEY')

url = 'https://api.rawg.io/api/genres?key={0}'.format(consumer_key)
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    print('Generos de videojuegos: ')
    for e in data['results']:
        print('***',e['name'],'*** Cantidad de juegos registrados: ',e['games_count'])