import requests

def postFunc(query, id):
    url = 'http://localhost:8080/api/addSuggestion/' + str(id)

    x = requests.post(url, json = query)