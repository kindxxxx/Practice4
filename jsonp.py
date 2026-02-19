import json

text = '{ "course": "Python", "level": 2, "passed": true }'

data = json.loads(text)

print(data["level"])



student = {
    "name": "Ayan",
    "age": 18,
    "active": True
}

result = json.dumps(student)

print(result)



data = {
    "city": "Almaty",
    "population": 2000000,
    "capital": False
}

print(json.dumps(data))



info = {
    "subject": "Programming",
    "credits": 5
}

with open("data.json", "w") as f:
    json.dump(info, f)



import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data["subject"])


