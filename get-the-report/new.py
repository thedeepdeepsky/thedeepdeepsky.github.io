import requests
response = requests.get(url='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita')
txt_file = open("wr.txt", "w")
txt_file.write(response)
txt_file.close()
