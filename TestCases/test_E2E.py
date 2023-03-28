import jsonpath
import json
import requests


def test_Add_new_data():
    app_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\lenovo\\PycharmProjects\\Dirako_Practice1\\Data_Users\\studentUpdate.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(app_URL, request_json)
    id = jsonpath.jsonpath(response.json(),'id')
    print(response.text)
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open("C:\\Users\\lenovo\\PycharmProjects\\Dirako_Practice1\\Data_Users\\techDetails.json", 'r')
    request_json = json.loads(file.read())
    response = requests.post(tech_api_url, request_json)
    print(response.text)
    #
    add_api_url = "https://thetestingworldapi.com/api/addresses"
    file = open("C:\\Users\\lenovo\\PycharmProjects\\Dirako_Practice1\\Data_Users\\address.json", 'r')
    request_json = json.loads(file.read())
    response = requests.post(add_api_url, request_json)
    #
    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/7390000"
    response = requests.get(final_details)
    print(response.text)
