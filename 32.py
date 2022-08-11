import requests
response = requests.get("http://localhost:5001")
expected = "hello and welcome to the world of moshe"
actual = response.text
print(actual)
assert expected == actual