# PUT and DELETE

import requests
import json

if __name__ == '__main__':
    # url = 'https://httpbin.org/post'
    url = 'https://httpbin.org/delete'
    payload = {'name': 'Luc', 'course': 'python', 'level': 'intermediate'}
    headers = { 'Content-Type' : 'application/json', 'access-token' : '12345' } #Se informa al servido que se estan enviando datos en formato json

    # response = requests.put(url, data= json.dumps(payload), headers=headers)
    response = requests.delete(url, data= json.dumps(payload), headers=headers)

    #json post se encarga de serializar los datos
    #data entonces debemos encargarnos de serializarlos nosotros
    print(response.url)

    if response.status_code == 200:
        # print(response.content)
        headers_response = response.headers # Lectura del Dic
        # print(headers_response)
        server = headers_response['Server']
        print(server)