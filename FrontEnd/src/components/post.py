import requests

def postSuggest(query, id):
    requests.post("http://localhost:8080/api/addSuggestion/" + str(id), data = query)

def postAsk(query, id):
    requests.post("http://localhost:8080/api/addAsk/" + str(id), data = query)