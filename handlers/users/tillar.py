import json
  

with open('languages.json','rb') as file:
    tillar = json.load(file)
    for til in tillar:
        print(f"{til['name']}:{til['code']}")
        # print(til['name'])