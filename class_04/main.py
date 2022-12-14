# POST

import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'name': 'Luc', 'course': 'python', 'level': 'intermediate'}
    
    response = requests.post(url, data= json.dumps(payload))

    #json post se encarga de serializar los datos
    #data entonces debemos encargarnos de serializarlos nosotros
    print(response.url)

    if response.status_code == 200:
        print(response.content)