import json
from pprint import pprint
with open('json2.json') as data:
    alldic = json.load(data)
    for i in alldic:
       for j in alldic[i]:
           for z in alldic[i][j]:
               print(alldic[i][j][z].get("answer"),"\n")