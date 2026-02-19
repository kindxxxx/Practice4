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



import json

data = {
    "city": "Almaty",
    "population": 2000000,
    "capital": False
}

print(json.dumps(data))

