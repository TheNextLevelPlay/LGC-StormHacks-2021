import requests

def postSuggest(query, id):
    requests.post("http://localhost:8080/api/addSuggestion/" + str(id), data = query)

def postAsk(query, id):
    requests.post("http://localhost:8080/api/addAsk/" + str(id), data = query)

def postResolveSuggest(query, id):
    requests.post("http://localhost:8080/api/rmSuggest/" + str(id), data = query)

def postResolveSuggestAll(id):
    requests.post("http://localhost:8080/api/resolveSuggest/" + str(id))

def postResolveAsk(query, id):
    requests.post("http://localhost:8080/api/rmAsk/" + str(id), data = query)

def postResolveAskAll(id):
    requests.post("http://localhost:8080/api/resolveAsk/" + str(id))
