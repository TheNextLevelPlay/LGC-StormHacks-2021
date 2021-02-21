import requests

def getSuggest(id):
    url = "http://localhost:8080/api/getSuggestion/" + str(id)
    print(url)
    return(requests.get(url).json())

def getAsk(id):
    url = "http://localhost:8080/api/getAsk/" + str(id)
    print(url)
    return(requests.get(url).json())

