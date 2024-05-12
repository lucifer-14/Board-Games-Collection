import json

ok = """
{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
"""

hello = {"name": "John Doe", "age": 30, "city": "New York"}

print(type(ok))
ok1 = json.loads(ok)
print(ok1, type(ok1))


print(type(hello))
hello1 = json.dumps(hello)
print(hello1, type(hello1))


with open('sample.json', 'r') as f:
    data = json.load(f)

print(data, type(data))
# json.loads()