import requests,json
response = requests.get(url='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita')
jsonstr=json.dumps(response,intend=4)
with open("wr.json") as k:
  k.write(jsonstr)
