# OBTENER JSON

import requests
import json

args = {}
name_value = input("Enter Name: ")
lastname_value = input("Enter Lastname: ")
# args["name"]=value
args = dict(name=name_value, lastname=lastname_value)

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        # response_json = response.json() #Dic
        # origin = response_json['origin']
        # print(origin)

        # Also you can import and use json library
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)