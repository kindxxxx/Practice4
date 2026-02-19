import json

text = '{ "course": "Python", "level": 2, "passed": true }'

data = json.loads(text)

print(data["level"])



import json

student = {
    "name": "Ayan",
    "age": 18,
    "active": True
}

result = json.dumps(student)

print(result)
