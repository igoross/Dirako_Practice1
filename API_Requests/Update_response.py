import json

import jsonpath
import requests

# API URL

url = "https://reqres.in/api/users/2"

# Read input Json File
file = open('C:\\Users\\lenovo\\Desktop\\API\\UserCreate.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)

# Make PUT req with json input body
response = requests.put(url, requests_json)

# Validating Response code
assert response.status_code ==200

# Parse response Content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])
