import json

import requests

# API URL

url = "https://reqres.in/api/users"

def test_create_new_user():

    # Read input Json File
    file = open('C:\\Users\\lenovo\\PycharmProjects\\Trello_Login_Automation\\DataUsers\\users.json', 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    print(requests_json)
    # Make POST req with json input body
    response = requests.post(url, requests_json)
    print(response.content)
    # validating response code
    assert response.status_code ==201
    print(response.status_code)
    # fetch header from response
    print(response.headers.get('Content-Length'))
    # Parse response to json format
    json.loads(response.text)