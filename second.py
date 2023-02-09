import json

with open('4questions.json') as json_f:
    questions4 = json.load(json_f)



owners = []
for x in range(len(questions4)):
    owners.append(questions4[x]["owner"])
print(owners)
