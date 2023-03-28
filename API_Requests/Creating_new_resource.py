import json

import jsonpath as jsonpath
import requests

# API URL

url = "http://thetestingworldapi.com/api/studentsDetails"

# Read input Json File
file = open('C:\\Users\\lenovo\\Desktop\\API\\StudentUpdate.json', 'r')
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
response_json = json.loads(response.text)

# pick ID useng json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])

