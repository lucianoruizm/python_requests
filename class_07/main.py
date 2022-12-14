# Descarga de imagen y almacenamiento

import requests
import json

if __name__ == '__main__':
    url = 'https://i.imgur.com/Q69YFcp.jpeg'

    response = requests.get(url, stream=True) #Realiaz la petición sin descargar el contenido
    with open('image.jpeg', 'wb') as file:
        for chunk in response.iter_content(): # Descarga el contenido del servidor poco a poco, por ejemplo archivos grandes como imagenes o pdf
            file.write(chunk)

    response.close()